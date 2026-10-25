# AQUÍ ESTOY --- Sistema de geolocalización y acompañamiento

> Proyecto académico de desarrollo de software.\
> MVP para apoyar el monitoreo de niños, niñas y adultos mayores
> mediante la ubicación GPS de un teléfono móvil.

## 1. Descripción

**AQUÍ ESTOY** es una solución de software orientada a que familiares o
cuidadores autorizados puedan consultar la ubicación de una persona
monitoreada y, en etapas posteriores, recibir alertas ante eventos
definidos como riesgosos.

La idea inicial contempla un dispositivo portátil. Para el producto
mínimo viable (MVP), se plantea utilizar un teléfono móvil como fuente
de GPS, validar el flujo de datos y luego evaluar hardware dedicado o
aplicaciones móviles nativas.

La ubicación de menores de edad y adultos mayores exige controles de
acceso, consentimiento y protección de datos desde el diseño.

## 2. Objetivo

Construir progresivamente una plataforma que permita registrar usuarios,
asociar personas monitoreadas y dispositivos, recibir coordenadas GPS,
definir zonas seguras, generar alertas y consultar un historial limitado
de ubicaciones.

## 3. Alcance del MVP

### Incluido en la primera etapa

-   Backend REST con FastAPI.
-   Conexión a la base de datos MySQL `aqui_estoy`.
-   Primer módulo de usuarios.
-   Pruebas manuales con Swagger UI y Postman.
-   Interfaz web inicial en HTML y CSS.
-   Preparación de la estructura para dispositivos, ubicaciones, zonas
    seguras y alertas.

### Fuera del alcance inicial

-   Fabricación o integración de una pulsera GPS física.
-   Aplicaciones móviles nativas.
-   Pasarela de pagos y cobros automáticos.
-   Envío productivo de SMS o notificaciones push.
-   Analítica avanzada y despliegue de alta disponibilidad.

Estos elementos podrán evaluarse después de validar el MVP.

## 4. Funcionalidades previstas

  -----------------------------------------------------------------------
  Módulo                  Propósito               Estado de referencia
  ----------------------- ----------------------- -----------------------
  Usuarios                Registrar y administrar Backend inicial en
                          usuarios                desarrollo

  Personas monitoreadas   Representar a la        Pendiente de integrar
                          persona cuya ubicación  
                          se consulta             

  Dispositivos            Registrar el teléfono   Flujo por implementar
                          que informa ubicación   

  Ubicaciones             Guardar coordenadas y   Flujo por implementar
                          metadatos               

  Zonas seguras           Definir zonas           Flujo por implementar
                          autorizadas             

  Alertas                 Registrar eventos de    Flujo por implementar
                          riesgo                  

  Notificaciones          Comunicar alertas a     Etapa posterior
                          responsables            

  Suscripciones y pagos   Administrar planes y    Fuera del MVP inicial
                          pagos                   
  -----------------------------------------------------------------------

## 5. Arquitectura conceptual

``` text
Teléfono móvil con GPS
        |
        | Coordenadas y datos del dispositivo
        v
Backend REST (FastAPI)
        |
        | SQLAlchemy
        v
Base de datos MySQL (aqui_estoy)
        ^
        |
Interfaz web / cuidador autorizado
        |
        v
Consulta de ubicación y alertas
```

El teléfono y la interfaz deben comunicarse con el backend mediante
endpoints definidos. La autorización debe comprobarse en el servidor, no
solamente en el frontend.

## 6. Tecnologías

-   **Python:** lenguaje del backend.
-   **FastAPI:** API REST.
-   **Uvicorn:** servidor ASGI para desarrollo.
-   **SQLAlchemy:** mapeo objeto-relacional.
-   **MySQL:** persistencia de datos.
-   **Pydantic:** validación de entrada y salida.
-   **python-dotenv:** variables de entorno.
-   **Swagger UI y Postman:** pruebas de la API.
-   **HTML y CSS:** interfaz web inicial.
-   **Git y GitHub:** control de versiones y colaboración.

Las dependencias y sus versiones deben registrarse en `requirements.txt`
cuando el equipo confirme el conjunto exacto utilizado.

## 7. Estructura del repositorio

``` text
Aqui_estoy/
├── backend/
│   ├── database/
│   │   └── conexion.py
│   ├── models/
│   │   ├── operaciones.py
│   │   └── usuario.py
│   ├── routers/
│   │   └── usuarios.py
│   ├── schema/
│   │   └── usuario.py
│   ├── .env                  # local; no publicar
│   ├── .gitignore
│   ├── main.py
│   └── probar_conexion.py
├── db/
│   ├── aqui_estoy.sql
│   └── aqui_estoy_diagrama.mwb
├── frontend/
│   ├── index.html
│   ├── inicio_sesion.html
│   ├── nuevo_usuario.html
│   ├── recuperar_contraseña.html
│   ├── css/
│   └── img/
└── README.md
```

La estructura puede cambiar durante el desarrollo. Verifica los nombres
y rutas reales en la rama de trabajo antes de ejecutar comandos.

### Archivos principales

-   `backend/main.py`: crea la aplicación FastAPI e incluye routers.
-   `backend/database/conexion.py`: configura la conexión y las sesiones
    de MySQL.
-   `backend/models/usuario.py`: modelo SQLAlchemy de la tabla
    `usuarios`.
-   `backend/models/operaciones.py`: operaciones de acceso a datos.
-   `backend/schema/usuario.py`: validación de datos y esquema de
    respuesta.
-   `backend/routers/usuarios.py`: rutas HTTP del módulo de usuarios.
-   `backend/probar_conexion.py`: prueba de conexión a MySQL.
-   `db/aqui_estoy.sql`: referencia SQL; verificar que corresponda al
    esquema activo antes de ejecutarlo.
-   `db/aqui_estoy_diagrama.mwb`: modelo visual de MySQL Workbench.
-   `frontend/`: páginas y estilos iniciales.

## 8. Requisitos previos

1.  Python instalado y accesible desde PowerShell.
2.  MySQL Server en ejecución.
3.  Base de datos `aqui_estoy` creada.
4.  Credenciales de MySQL con permisos necesarios.
5.  Git instalado.
6.  Postman o un navegador para probar la API.

Los comandos de esta guía están escritos para PowerShell en Windows.

## 9. Configurar el entorno

### 9.1 Entrar al backend

Desde la raíz del proyecto:

``` powershell
cd backend
```

### 9.2 Crear un entorno virtual (recomendado)

``` powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell impide activar el entorno, no cambies políticas del
sistema sin revisar primero la configuración. Puedes usar directamente
`.\.venv\Scripts\python.exe`.

### 9.3 Instalar dependencias

Si existe `requirements.txt`:

``` powershell
python -m pip install -r requirements.txt
```

Si no existe, confirma las dependencias utilizadas por los imports y
registra sus versiones. El backend ha utilizado paquetes como FastAPI,
Uvicorn, SQLAlchemy, un controlador MySQL, python-dotenv y
email-validator. No instales paquetes adicionales sin comprobar que sean
necesarios.

### 9.4 Variables de entorno

Crea `backend/.env` localmente con las variables que lee
`database/conexion.py`:

``` dotenv
DB_USER=tu_usuario_mysql
DB_PASSWORD=tu_contrasena_mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=aqui_estoy
```

Reemplaza los valores de ejemplo por los de tu entorno. Nunca publiques
credenciales reales en el README, capturas públicas o repositorios.

## 10. Base de datos

La base de datos usada por el backend se llama `aqui_estoy`.

Antes de importar un archivo SQL, confirma que no vaya a sobrescribir ni
recrear objetos existentes. `db/aqui_estoy.sql` es una referencia y
podría no representar todas las tablas de la base activa.

La tabla `usuarios` comprobada en MySQL Workbench contiene:

  Campo                   Descripción
  ----------------------- ----------------------------------------------------------
  `id`                    Clave primaria autoincremental (`BIGINT UNSIGNED`)
  `nombres`               Nombres del usuario
  `apellidos`             Apellidos del usuario
  `tipo_documento`        `CC`, `TI`, `CE`, `PASAPORTE` u `OTRO`
  `documento_identidad`   Número del documento
  `telefono`              Teléfono de contacto
  `correo`                Correo único
  `estado`                `activo`, `inactivo` o `bloqueado`; por defecto `activo`
  `parentesco`            `madre`, `padre`, `hijo`, `abuela` u `otro`

La base contempla también áreas como dispositivos, ubicaciones, zonas
seguras, alertas, notificaciones, suscripciones y pagos. Antes de
implementar cada módulo, verifica en MySQL Workbench la estructura real
y las claves foráneas. Los modelos SQLAlchemy deben coincidir con las
tablas existentes.

## 11. Ejecutar el backend

Con la terminal ubicada en `Aqui_estoy/backend`:

``` powershell
python -m uvicorn main:app --reload
```

Direcciones locales:

-   API: `http://127.0.0.1:8000/`
-   Documentación interactiva: `http://127.0.0.1:8000/docs`
-   Documentación alternativa: `http://127.0.0.1:8000/redoc`

Detén el servidor con `Ctrl + C`.

**Importante:** ejecuta `main:app` desde la carpeta `backend`, porque
allí está `main.py`. Ejecutarlo desde la raíz puede producir
`Could not import module "main"`.

## 12. Probar la API

### Swagger UI

1.  Inicia Uvicorn.
2.  Abre `http://127.0.0.1:8000/docs`.
3.  Revisa las rutas disponibles.
4.  Selecciona una ruta, pulsa **Try it out**, introduce datos de prueba
    y ejecuta.
5.  Comprueba el código HTTP y el cuerpo de respuesta.

### Postman

Se recomienda crear una colección llamada `AQUI ESTOY - API local`. Para
usuarios, documentar y probar progresivamente:

-   Crear usuario.
-   Consultar todos los usuarios.
-   Consultar por identificador.
-   Actualizar usuario.
-   Eliminar usuario.

No asumas que todos esos endpoints están implementados: las rutas
disponibles dependen de `backend/routers/usuarios.py`.

Usa datos ficticios. La tabla impone unicidad al correo y a la
combinación de tipo y número de documento; los duplicados deben
manejarse con respuestas de error controladas.

## 13. Áreas del modelo de datos

-   **Usuarios y miembros de cuenta:** responsables y participantes
    autorizados.
-   **Personas monitoreadas:** personas cuya ubicación se consulta.
-   **Dispositivos:** teléfonos u otros dispositivos que informan
    ubicación.
-   **Ubicaciones e historial:** coordenadas y metadatos recibidos.
-   **Zonas seguras:** lugares o perímetros definidos como seguros.
-   **Alertas y notificaciones:** eventos y avisos.
-   **Suscripciones, moras y pagos:** gestión comercial futura.

Verifica las relaciones en la base activa y en el modelo de MySQL
Workbench. No deduzcas una clave foránea solo por el nombre de una
columna.

## 14. Seguridad y privacidad

La ubicación de niños y adultos mayores requiere protección especial.
Como mínimo:

-   No subir `.env` ni credenciales al repositorio.
-   Utilizar credenciales de base de datos robustas.
-   No devolver contraseñas ni hashes en las respuestas de la API.
-   Implementar autenticación y autorización antes de exponer datos
    reales.
-   Permitir que cada responsable consulte solo a las personas
    autorizadas.
-   Validar datos en el backend.
-   No registrar tokens, contraseñas ni coordenadas personales
    innecesarias en logs.
-   Usar HTTPS antes de desplegar públicamente.
-   Definir consentimiento, acceso, retención y eliminación de datos.
-   Limitar el historial al periodo establecido en los requisitos.

**El proyecto está en desarrollo y no debe considerarse listo para
producción ni utilizarse para monitorear personas reales hasta
implementar y probar los controles de seguridad y autorización.**

## 15. Flujo de trabajo con Git

Estrategia sugerida:

-   `main`: versión estable.
-   `dev`: integración de funcionalidades.
-   Ramas de trabajo: por ejemplo, `feature/crud-usuarios` o
    `fix/modelo-usuarios`.

Ejemplo:

``` powershell
git status
git switch dev
git pull origin dev
git switch -c feature/crud-usuarios
```

Después de realizar cambios:

``` powershell
git status
git add backend README.md
git commit -m "docs: documenta el proyecto y el backend"
git push -u origin feature/crud-usuarios
```

Abre un Pull Request hacia `dev` para revisión. Integra a `main` cuando
la versión haya sido revisada y probada. Si el equipo usa otra
estrategia, acuerden y documenten una sola.

Antes de `git add`, revisa `git status` y confirma que no se incluyan
`.env`, contraseñas, archivos temporales o datos personales.

## 16. Plan de desarrollo recomendado

1.  Alinear los modelos SQLAlchemy con las tablas reales.
2.  Completar el CRUD de usuarios y manejar errores y restricciones
    únicas.
3.  Probar y documentar el CRUD en Postman.
4.  Definir autenticación y autorización.
5.  Modelar las relaciones entre cuentas, personas y dispositivos.
6.  Recibir ubicación desde un teléfono y validar las coordenadas.
7.  Consultar última ubicación e historial y establecer la retención.
8.  Implementar zonas seguras y alertas.
9.  Conectar la interfaz web con la API.
10. Ejecutar pruebas funcionales, de seguridad y de errores.

## 17. Estado y limitaciones conocidas

Este README documenta la estructura identificada durante el desarrollo;
no sustituye la verificación del código actual.

-   FastAPI y la conexión a MySQL forman parte del backend inicial.
-   El módulo de usuarios tiene modelos, esquemas, operaciones y un
    router en desarrollo.
-   La tabla `usuarios` confirmada no contiene `fecha_nacimiento`,
    `contrasena_hash`, `ultimo_acceso`, `creado_en` ni `actualizado_en`.
-   La tabla sí contiene `parentesco`, que debe reflejarse en el modelo.
-   La creación de usuarios y el resto del CRUD deben probarse contra la
    base de datos real.
-   La tabla actual no almacena contraseñas. El inicio de sesión debe
    diseñarse antes de implementarse; nunca se deben guardar contraseñas
    en texto plano.
-   GPS, zonas seguras, alertas e historial son objetivos del MVP que
    requieren implementación y pruebas.
-   El archivo SQL puede estar incompleto o desactualizado. No lo
    ejecutes sobre una base con datos sin revisar su contenido y contar
    con una copia de seguridad.

## 18. Equipo y contribuciones

El proyecto se desarrolla de manera colaborativa. Se recomienda que cada
integrante:

-   Trabaje en una rama asignada.
-   Realice cambios pequeños con mensajes de commit descriptivos.
-   Actualice la documentación cuando cambien la arquitectura, el
    esquema o los endpoints.
-   Pruebe los cambios antes de abrir un Pull Request.
-   No comparta credenciales ni datos reales de personas monitoreadas.

## Licencia

La licencia debe definirse por el equipo. Hasta que exista una decisión
explícita, este README no declara una licencia de distribución.
