# Diccionario de datos — AQUÍ ESTOY

## 1. Objetivo

Este documento describe las tablas y los campos de la base de datos `aqui_estoy`, utilizada por el sistema de geolocalización AQUÍ ESTOY.

La base de datos tiene como finalidad organizar la información de los usuarios, los dispositivos, las ubicaciones, las zonas seguras, las notificaciones y los datos relacionados con las suscripciones y los pagos.

## 2. Motor de base de datos

- Motor: MySQL.
- Base de datos: `aqui_estoy`.
- Acceso desde el backend: SQLAlchemy.
- Archivo de referencia: `db/aqui_estoy.sql`.
- Modelo visual de referencia: `db/aqui_estoy_diagrama.mwb`.

**Nota:** este diccionario se basa en la estructura identificada en los archivos del proyecto. Antes de utilizarlo como documentación definitiva, se debe contrastar con la estructura actual de MySQL Workbench. No se deben crear, eliminar ni modificar columnas únicamente para hacer coincidir este documento.

## 3. Tabla `usuarios`

### Descripción

Almacena información básica de los usuarios registrados en el sistema.

| Campo | Tipo identificado | Descripción |
|---|---|---|
| `id` | BIGINT UNSIGNED | Identificador único del usuario. |
| `nombres` | VARCHAR(80) | Nombres del usuario. |
| `apellidos` | VARCHAR(80) | Apellidos del usuario. |
| `tipo_documento` | ENUM | Tipo de documento: CC, TI, CE, PASAPORTE u OTRO, según el esquema. |
| `documento_identidad` | VARCHAR(20) | Número del documento de identidad. |
| `telefono` | VARCHAR(20) | Número de contacto. |
| `correo` | VARCHAR(150) | Correo electrónico del usuario. |
| `estado` | ENUM | Estado de la cuenta, según los valores definidos en la base de datos. |
| `parentesco` | Pendiente de verificar | Relación familiar, si existe en la tabla actual. |

### Restricciones identificadas

- `id` es la clave primaria.
- El correo tiene una restricción de unicidad en el esquema SQL identificado.
- El documento puede tener una restricción única compuesta con el tipo de documento, según el esquema SQL identificado.

### Observación importante

El modelo Python `backend/models/usuario.py` contiene campos adicionales, entre ellos `fecha_nacimiento`, `contrasena_hash`, `ultimo_acceso`, `creado_en` y `actualizado_en`.

Estos campos no aparecen todos en la definición de `usuarios` del archivo SQL revisado. Se debe verificar cuál es la estructura real de la base de datos antes de ajustar el modelo o el esquema.

## 4. Tabla `dispositivos`

### Descripción

Representa los dispositivos que se utilizan como fuente de ubicación de las personas monitoreadas.

| Campo o atributo | Descripción |
|---|---|
| Identificador | Identifica el dispositivo. El nombre y tipo exactos del campo deben verificarse en MySQL. |
| Información del dispositivo | Datos que permiten reconocer el dispositivo registrado. Los campos exactos deben verificarse. |
| Estado | Estado del dispositivo, si está definido en el esquema actual. |

**Pendiente:** confirmar los nombres, tipos, claves y restricciones de las columnas de esta tabla.

## 5. Tabla `ubicaciones`

### Descripción

Almacena coordenadas y datos de posicionamiento asociados a un dispositivo y, según el esquema identificado, a un usuario.

| Campo | Tipo o dato identificado | Descripción |
|---|---|---|
| `dispositivos_id` | Pendiente de confirmar tipo exacto | Referencia al dispositivo asociado a la ubicación. |
| `usuarios_id` | Pendiente de confirmar tipo exacto | Referencia al usuario asociado, según el esquema SQL. |
| `latitud` | Pendiente de confirmar | Coordenada geográfica de latitud. |
| `longitud` | Pendiente de confirmar | Coordenada geográfica de longitud. |
| `precision_m` | Pendiente de confirmar | Precisión estimada de la ubicación en metros. |
| `altitud_m` | Pendiente de confirmar | Altitud estimada en metros. |
| `velocidad_kmh` | Pendiente de confirmar | Velocidad registrada en kilómetros por hora. |
| `rumbo_grados` | Pendiente de confirmar | Dirección del desplazamiento en grados. |
| `nivel_bateria` | Pendiente de confirmar | Nivel de batería reportado por el dispositivo. |

**Pendiente:** verificar si la tabla actual contiene un campo de fecha y hora para cada ubicación. Este dato es necesario para ordenar el historial y consultar las últimas 72 horas.

## 6. Tabla `zonas_seguras`

### Descripción

Representa las áreas geográficas definidas como seguras para una persona monitoreada.

Uso previsto:

- Registrar zonas autorizadas.
- Definir sus límites geográficos.
- Asociar las zonas con las personas correspondientes.
- Permitir la detección de entradas o salidas de dichas zonas.

Los nombres y tipos exactos de sus columnas deben confirmarse en la base de datos actual.

## 7. Tabla `notificaciones`

### Descripción

Almacena o gestiona las notificaciones generadas por el sistema.

Uso previsto:

- Informar sobre eventos relacionados con la geolocalización.
- Comunicar salidas de zonas seguras.
- Registrar eventos de pérdida de comunicación.
- Facilitar la consulta de alertas por los usuarios autorizados.

Se debe verificar si la tabla incluye fecha de generación, destinatario, tipo, estado de lectura y relación con la persona monitoreada.

## 8. Tabla `suscripciones`

### Descripción

Contiene información relacionada con las suscripciones de las cuentas, si la funcionalidad está habilitada en el esquema actual.

Su estructura exacta, restricciones y relación con los usuarios deben verificarse en MySQL Workbench.

La gestión de pagos y suscripciones no forma parte de las funcionalidades prioritarias del MVP, salvo que se acuerde expresamente lo contrario.

## 9. Tabla `pagos`

### Descripción

Contiene información relacionada con los pagos asociados al sistema.

Su estructura exacta, campos de valor, fecha, estado y relación con las suscripciones deben verificarse en la base de datos actual.

La integración con una pasarela de pagos se considera una funcionalidad futura.

## 10. Relaciones entre tablas

Las relaciones deben confirmarse mediante las claves foráneas de la base de datos real.

Relaciones previstas conceptualmente:

- Un usuario puede estar asociado a uno o varios dispositivos, según las reglas del sistema.
- Un dispositivo puede generar múltiples registros de ubicación.
- Una persona monitoreada puede estar asociada a una o varias zonas seguras.
- El sistema puede generar múltiples notificaciones.
- Una suscripción puede estar relacionada con uno o varios registros de pago, dependiendo del modelo definitivo.

Estas relaciones describen el comportamiento previsto y no sustituyen la verificación de las claves foráneas reales.

## 11. Consulta para verificar las columnas

En MySQL Workbench, seleccionar la base de datos y ejecutar:

```sql
USE aqui_estoy;

SHOW TABLES;

DESCRIBE usuarios;
DESCRIBE dispositivos;
DESCRIBE ubicaciones;
DESCRIBE zonas_seguras;
DESCRIBE notificaciones;
DESCRIBE suscripciones;
DESCRIBE pagos;
```

Para revisar las claves foráneas:

```sql
SELECT
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'aqui_estoy'
  AND REFERENCED_TABLE_NAME IS NOT NULL
ORDER BY TABLE_NAME, COLUMN_NAME;
```

## 12. Mantenimiento del diccionario

Cada vez que se modifique la estructura de la base de datos, se debe actualizar este documento para mantenerlo sincronizado con MySQL Workbench, el archivo SQL y los modelos del backend.

No se deben documentar campos como implementados hasta confirmar su existencia en la base de datos.
