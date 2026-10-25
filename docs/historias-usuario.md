# Historias de usuario — AQUÍ ESTOY

## 1. Objetivo

Definir las necesidades de los usuarios de AQUÍ ESTOY mediante historias de usuario que permitan planificar, desarrollar y validar las funcionalidades del sistema.

Las historias describen el comportamiento esperado. No significa que todas las funcionalidades estén implementadas actualmente.

## 2. Actores del sistema

### Acudiente o administrador familiar

Persona autorizada para registrar y administrar la cuenta, asociar personas monitoreadas y consultar sus ubicaciones.

### Persona monitoreada

Niño o adulto mayor cuya ubicación se registra mediante un dispositivo autorizado.

### Sistema

Componente encargado de procesar las ubicaciones, verificar las zonas seguras y generar alertas cuando se cumplan las condiciones establecidas.

## 3. Historias de usuario prioritarias

### HU-01. Registro de usuario

**Como** visitante,

**quiero** registrar una cuenta con mis datos personales,

**para** acceder a las funcionalidades de AQUÍ ESTOY.

**Criterios de aceptación:**

- El sistema valida los campos obligatorios.
- El correo debe tener un formato válido.
- El sistema debe evitar registros duplicados según las restricciones definidas.
- La contraseña debe almacenarse mediante un hash seguro.
- El sistema informa si el registro se realiza correctamente o si existe un error.

**Prioridad:** Alta.

### HU-02. Inicio de sesión

**Como** usuario registrado,

**quiero** iniciar sesión de forma segura,

**para** acceder únicamente a la información autorizada.

**Criterios de aceptación:**

- El usuario debe proporcionar sus credenciales.
- Las credenciales incorrectas no deben permitir el acceso.
- Las respuestas no deben revelar la contraseña ni su hash.
- Las funcionalidades privadas deben exigir una autenticación válida.

**Prioridad:** Alta.

**Estado:** Pendiente de verificar la implementación del inicio de sesión en el backend.

### HU-03. Registro de una persona monitoreada

**Como** acudiente,

**quiero** registrar a un niño o adulto mayor que esté bajo mi cuidado,

**para** asociarlo con el servicio de geolocalización.

**Criterios de aceptación:**

- El sistema solicita la información definida como obligatoria.
- La persona queda asociada a la cuenta autorizada.
- Se valida que el usuario tenga permiso para administrar esa persona.
- La información se almacena correctamente.

**Prioridad:** Alta.

### HU-04. Asociación de un dispositivo

**Como** acudiente,

**quiero** asociar un teléfono celular a una persona monitoreada,

**para** utilizarlo como fuente de su ubicación GPS.

**Criterios de aceptación:**

- El sistema permite registrar o seleccionar un dispositivo.
- El dispositivo queda relacionado con la persona correspondiente.
- Se identifica el estado del dispositivo cuando esa información esté disponible.
- Un dispositivo no autorizado no debe enviar ubicaciones a una cuenta ajena.

**Prioridad:** Alta.

### HU-05. Captura de ubicación GPS

**Como** acudiente,

**quiero** que el sistema reciba las coordenadas del teléfono autorizado,

**para** conocer la ubicación reportada de la persona monitoreada.

**Criterios de aceptación:**

- El teléfono solicita los permisos de geolocalización necesarios.
- Se obtienen latitud y longitud cuando el dispositivo y el navegador lo permiten.
- El sistema valida que las coordenadas sean válidas.
- La API almacena la ubicación junto con la fecha y hora del registro.
- Si no hay permiso, conexión o señal disponible, el sistema informa la limitación.

**Prioridad:** Alta.

### HU-06. Consulta de última ubicación

**Como** acudiente autorizado,

**quiero** consultar la última ubicación registrada de una persona,

**para** conocer dónde fue detectada por última vez.

**Criterios de aceptación:**

- El sistema muestra la última ubicación disponible.
- Se presenta la fecha y hora del registro.
- Si la ubicación está desactualizada, se informa al usuario.
- Solo los usuarios autorizados pueden consultar la información.

**Prioridad:** Alta.

### HU-07. Definición de zonas seguras

**Como** acudiente,

**quiero** definir zonas seguras para una persona monitoreada,

**para** establecer áreas en las que se espera que permanezca.

**Criterios de aceptación:**

- El sistema permite registrar una zona con sus límites geográficos.
- La zona queda asociada a la persona correspondiente.
- Se validan los datos necesarios para definir la zona.
- El sistema permite consultar las zonas registradas.

**Prioridad:** Alta.

### HU-08. Alerta por salida de una zona segura

**Como** acudiente,

**quiero** recibir una alerta cuando una persona salga de una zona segura,

**para** reaccionar oportunamente ante una situación de riesgo.

**Criterios de aceptación:**

- El sistema compara las ubicaciones recibidas con las zonas configuradas.
- Se genera una alerta cuando se cumplen las condiciones de salida definidas.
- La alerta identifica a la persona y la zona relacionada.
- El sistema evita generar alertas repetidas innecesarias para el mismo evento.

**Prioridad:** Alta.

### HU-09. Detección de pérdida de comunicación

**Como** acudiente,

**quiero** conocer si un dispositivo deja de reportar ubicaciones,

**para** saber cuándo no puedo confiar en la actualidad de la información.

**Criterios de aceptación:**

- El sistema identifica cuándo una ubicación supera el tiempo máximo definido.
- La interfaz diferencia una ubicación reciente de una ubicación desactualizada.
- Cuando corresponda, se genera una alerta de desconexión.
- El tiempo máximo sin reportes debe ser configurable o estar definido por una regla de negocio.

**Prioridad:** Media.

### HU-10. Consulta del historial de ubicaciones

**Como** acudiente autorizado,

**quiero** consultar las ubicaciones registradas durante las últimas 72 horas,

**para** revisar los desplazamientos recientes de la persona monitoreada.

**Criterios de aceptación:**

- El sistema consulta los registros dentro del periodo permitido.
- Las ubicaciones aparecen ordenadas por fecha y hora.
- Se muestran los datos necesarios para interpretar cada registro.
- El sistema no presenta registros anteriores al periodo establecido como parte del historial disponible para el MVP.

**Prioridad:** Alta.

### HU-11. Gestión de información del usuario

**Como** usuario registrado,

**quiero** consultar y actualizar mis datos permitidos,

**para** mantener mi información al día.

**Criterios de aceptación:**

- El sistema valida los campos actualizados.
- No permite modificar información para la que el usuario no tenga autorización.
- Los cambios se guardan correctamente.
- Los errores se presentan de forma comprensible.

**Prioridad:** Media.

### HU-12. Consulta del estado del dispositivo

**Como** acudiente,

**quiero** conocer el estado de conexión y la batería reportada por el dispositivo cuando esté disponible,

**para** anticipar posibles interrupciones en la geolocalización.

**Criterios de aceptación:**

- El sistema muestra el último estado conocido.
- La información incluye la fecha del último reporte.
- Si el dispositivo no suministra el nivel de batería, el sistema no inventa el valor.
- Se diferencia entre un dato no disponible y un nivel de batería bajo.

**Prioridad:** Media.

## 4. Funcionalidades futuras

Las siguientes historias pueden incorporarse después de validar el MVP:

- **HU-13. Gestión de suscripciones:** como administrador de una cuenta, quiero consultar el estado de mi suscripción para conocer las condiciones del servicio.
- **HU-14. Gestión de pagos:** como usuario, quiero consultar los pagos asociados a mi cuenta para revisar su estado.
- **HU-15. Integración con dispositivo dedicado:** como acudiente, quiero utilizar un dispositivo GPS específico para monitorear a una persona sin depender exclusivamente de un teléfono celular.

Estas funcionalidades no deben considerarse terminadas hasta que se implementen y prueben.

## 5. Orden recomendado de desarrollo

1. Validar la conexión con MySQL y el modelo de usuarios.
2. Confirmar el registro y la gestión básica de usuarios.
3. Implementar autenticación y autorización.
4. Implementar el registro y la asociación de personas monitoreadas.
5. Implementar la asociación del dispositivo.
6. Registrar y consultar ubicaciones GPS.
7. Implementar zonas seguras.
8. Generar alertas.
9. Consultar el historial de 72 horas.
10. Realizar pruebas funcionales y de seguridad.

## 6. Validación de las historias

Una historia se considera terminada cuando:

- Cumple todos sus criterios de aceptación.
- Se ha probado mediante solicitudes a la API o desde la interfaz, según corresponda.
- No expone información privada a usuarios no autorizados.
- Los errores se gestionan de manera controlada.
- La documentación del proyecto está actualizada.
