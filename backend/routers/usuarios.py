from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database.conexion import obtener_db
from schema.usuario import UsuarioActualizar, UsuarioCrear, UsuarioRespuesta, UsuarioLogin
from seguridad import hashear_contrasena, verificar_contrasena
from models.operaciones import (
    actualizar_usuario,
    consultar_usuario,
    consultar_usuarios,
    crear_usuario,
    eliminar_usuario,
    consultar_usuario_por_correo,
)


router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


# CREAR USUARIO 
def registrar_usuario(
    datos: UsuarioCrear,
    db: Session = Depends(obtener_db)
):
    try:
        # La contraseña en texto plano nunca llega a la base de datos
        datos_usuario = datos.model_dump(exclude={"contrasena"})
        datos_usuario["contrasena_hash"] = hashear_contrasena(datos.contrasena)

        return crear_usuario(db, datos_usuario)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El correo o documento puede estar registrado."
        )

# INICIAR SESIÓN
@router.post("/login", response_model=UsuarioRespuesta)
def iniciar_sesion(
    datos: UsuarioLogin,
    db: Session = Depends(obtener_db)
):
    usuario = consultar_usuario_por_correo(db, datos.correo)

    hash_guardado = usuario.contrasena_hash if usuario else None
    contrasena_valida = verificar_contrasena(datos.contrasena, hash_guardado)

    # Mismo mensaje para correo inexistente y contraseña incorrecta
    if not usuario or not hash_guardado or not contrasena_valida:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos."
        )

    if usuario.estado != "activo":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="La cuenta no está activa."
        )

    return usuario


# LEER (TODOS LOS USUARIOS)
@router.get("/", response_model=list[UsuarioRespuesta])
def listar_usuarios(db: Session = Depends(obtener_db)):
    return consultar_usuarios(db)


# LEER (UN USUARIO)
@router.get("/{usuario_id}", response_model=UsuarioRespuesta)
def obtener_usuario(
    usuario_id: int,
    db: Session = Depends(obtener_db)
):
    usuario = consultar_usuario(db, usuario_id)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado."
        )

    return usuario


# ACTUALIZAR
@router.put("/{usuario_id}", response_model=UsuarioRespuesta)
def modificar_usuario(
    usuario_id: int,
    datos: UsuarioActualizar,
    db: Session = Depends(obtener_db)
):
    usuario = consultar_usuario(db, usuario_id)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado."
        )

    cambios = datos.model_dump(exclude_unset=True)

    if not cambios:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se enviaron datos para actualizar."
        )

    try:
        return actualizar_usuario(db, usuario, cambios)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El correo o documento puede estar registrado."
        )


# ELIMINAR
@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def borrar_usuario(
    usuario_id: int,
    db: Session = Depends(obtener_db)
):
    usuario = consultar_usuario(db, usuario_id)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado."
        )

    try:
        eliminar_usuario(db, usuario)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No se puede eliminar: el usuario tiene registros asociados."
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)