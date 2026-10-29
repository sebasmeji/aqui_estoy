from pwdlib import PasswordHash

_hasher = PasswordHash.recommended()

# Hash de relleno: se verifica cuando el correo no existe, para que la
# respuesta tarde lo mismo y no revele qué correos están registrados.
_HASH_FALSO = _hasher.hash("contrasena-de-relleno")


def hashear_contrasena(contrasena: str) -> str:
    return _hasher.hash(contrasena)


def verificar_contrasena(contrasena: str, hash_guardado: str | None) -> bool:
    return _hasher.verify(contrasena, hash_guardado or _HASH_FALSO)