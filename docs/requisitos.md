# Requisitos del sistema — AQUÍ ESTOY

## 1. Descripción del proyecto

AQUÍ ESTOY es un sistema de geolocalización diseñado para apoyar el cuidado y monitoreo de niños y adultos mayores mediante dispositivos móviles.

El sistema busca que un acudiente o familiar autorizado pueda consultar ubicaciones, establecer zonas seguras y recibir alertas cuando ocurran situaciones definidas como relevantes para la seguridad de la persona monitoreada.

La primera versión funcional utilizará un teléfono celular como fuente de ubicación GPS. La integración con una pulsera u otro dispositivo dedicado se contempla como una evolución futura.

## 2. Problema identificado

Los familiares y cuidadores pueden tener dificultades para conocer la ubicación reciente de las personas bajo su cuidado, especialmente cuando estas se desplazan de manera independiente.

La falta de información actualizada puede dificultar la reacción oportuna ante salidas de zonas seguras o interrupciones en la comunicación.

AQUÍ ESTOY propone centralizar la información de ubicación y proporcionar mecanismos de consulta y alertas, respetando los permisos de acceso y la privacidad de las personas.

## 3. Objetivo general

Desarrollar una aplicación web con backend y base de datos que permita registrar personas monitoreadas, recibir y consultar sus ubicaciones GPS, administrar zonas seguras y generar alertas para usuarios autorizados.

## 4. Objetivos específicos

- Gestionar el registro y la información básica de los usuarios.
- Relacionar las cuentas autorizadas con las personas monitoreadas.
- Permitir la asociación de un dispositivo móvil como fuente de ubicación.
- Almacenar y consultar las coordenadas GPS recibidas.
- Definir zonas seguras y detectar eventos relacionados con sus límites.
- Generar alertas ante eventos definidos como relevantes.
- Permitir la consulta del historial de ubicaciones de las últimas 72 horas.
- Proteger la información personal y geográfica almacenada.

## 5. Alcance del MVP

La primera versión funcional priorizará:

1. Conexión entre FastAPI y MySQL.
2. Registro y gestión básica de usuarios.
3. Autenticación y autorización de acceso.
4. Registro de personas monitoreadas.
5. Asociación de un teléfono celular.
6. Captura y almacenamiento de coordenadas GPS.
7. Consulta de la última ubicación disponible.
8. Registro de zonas seguras.
9. Generación de alertas por salida de zonas seguras.
10. Detección de ubicaciones desactualizadas.
11. Consulta del historial de ubicaciones de las últimas 72 horas.

El orden de implementación podrá ajustarse según los resultados de las pruebas y las dependencias técnicas.

## 6. Fuera del alcance inicial

Se consideran funcionalidades futuras, salvo decisión expresa del equipo:

- Fabricación o integración de una pulsera GPS dedicada.
- Aplicaciones móviles nativas independientes.
- Integración con una pasarela real de pagos.
- Envío de SMS o notificaciones push mediante proveedores externos.
- Analítica avanzada y predicción de desplazamientos.
- Integraciones con servicios externos no requeridos para demostrar el MVP.

## 7. Requisitos funcionales

### RF-01. Registro de usuarios

El sistema debe permitir registrar usuarios mediante un formulario con los campos obligatorios definidos para el proyecto.

### RF-02. Validación de usuarios

El sistema debe validar los datos recibidos y evitar duplicados de acuerdo con las restricciones establecidas para el correo y el documento de identidad.

### RF-03. Autenticación

El sistema debe permitir que los usuarios registrados se autentiquen antes de acceder a las funcionalidades privadas.

### RF-04. Autorización

El sistema debe comprobar que cada usuario tenga permiso para consultar o modificar la información solicitada.

### RF-05. Gestión de personas monitoreadas

El sistema debe permitir registrar y administrar las personas que serán monitoreadas por un acudiente autorizado.

### RF-06. Asociación de dispositivos

El sistema debe permitir asociar un dispositivo autorizado con la persona monitoreada correspondiente.

### RF-07. Recepción de coordenadas

El sistema debe recibir las coordenadas GPS enviadas por un dispositivo autorizado y validar sus valores.

### RF-08. Almacenamiento de ubicaciones

El sistema debe almacenar las ubicaciones recibidas con la información temporal necesaria para identificar cuándo fueron registradas.

### RF-09. Consulta de última ubicación

El sistema debe permitir consultar la última ubicación disponible de una persona monitoreada.

### RF-10. Gestión de zonas seguras

El sistema debe permitir crear, consultar y administrar las zonas seguras definidas para una persona monitoreada.

### RF-11. Detección de salida de zona

El sistema debe identificar cuándo una ubicación recibida indica que la persona salió de una zona segura, de acuerdo con las reglas configuradas.

### RF-12. Generación de alertas

El sistema debe generar alertas cuando se cumplan las condiciones de riesgo definidas para el MVP.

### RF-13. Detección de falta de actualización

El sistema debe identificar cuándo un dispositivo deja de reportar ubicaciones durante el tiempo establecido por la regla correspondiente.

### RF-14. Consulta del historial

El sistema debe permitir consultar el historial de ubicaciones de las últimas 72 horas.

### RF-15. Gestión de información personal

El sistema debe permitir consultar y actualizar los datos personales autorizados de cada usuario.

### RF-16. Consulta del estado del dispositivo

El sistema debe mostrar la última información disponible sobre el estado del dispositivo y su batería cuando estos datos sean proporcionados.

### RF-17. Manejo de errores

El sistema debe responder a solicitudes inválidas, fallos de conexión y errores de procesamiento mediante mensajes controlados, sin exponer información sensible.

**Nota:** estos requisitos representan el comportamiento esperado. Su implementación debe verificarse mediante pruebas.

## 8. Requisitos no funcionales

### RNF-01. Seguridad

La información personal y de ubicación debe estar protegida contra accesos no autorizados. Las contraseñas deben almacenarse mediante un mecanismo de hash seguro.

### RNF-02. Privacidad

El acceso a las ubicaciones debe limitarse a las personas autorizadas. El tratamiento de datos de niños y adultos mayores debe respetar las autorizaciones y obligaciones legales aplicables.

### RNF-03. Rendimiento

Las operaciones frecuentes, como consultar la última ubicación, deben responder en un tiempo adecuado para el uso esperado del MVP. El tiempo objetivo debe definirse y validarse mediante pruebas de rendimiento.

### RNF-04. Disponibilidad

El sistema debe estar disponible durante los periodos de operación previstos. La disponibilidad objetivo y el procedimiento de recuperación deben definirse cuando se establezca el ambiente de despliegue.

### RNF-05. Integridad de datos

El sistema debe validar los datos recibidos y mantener la consistencia de las relaciones entre usuarios, dispositivos, personas monitoreadas y ubicaciones.

### RNF-06. Mantenibilidad

El código debe estar organizado en módulos con responsabilidades claras, de manera que se puedan corregir errores y añadir funcionalidades sin modificar innecesariamente los componentes existentes.

### RNF-07. Usabilidad

La interfaz debe presentar información clara, formularios comprensibles y mensajes de error que orienten al usuario.

### RNF-08. Compatibilidad

La interfaz web debe probarse en los navegadores que el equipo decida soportar. Las funciones de geolocalización deben tener en cuenta los permisos y las limitaciones del navegador y del dispositivo.

### RNF-09. Escalabilidad

La arquitectura debe permitir añadir nuevas funcionalidades y aumentar gradualmente la cantidad de usuarios y ubicaciones sin exigir una reconstrucción completa del sistema.

### RNF-10. Trazabilidad

Los errores y eventos técnicos relevantes deben poder diagnosticarse mediante registros de aplicación que no expongan contraseñas, tokens ni información privada innecesaria.

### RNF-11. Retención de ubicaciones

El sistema debe ofrecer un historial consultable de las últimas 72 horas para el alcance definido del MVP. La política de conservación y eliminación de datos debe establecerse de forma explícita.

### RNF-12. Recuperación ante errores

Los errores de conexión con la base de datos y las fallas de comunicación deben gestionarse sin provocar respuestas que expongan detalles internos o datos sensibles.

## 9. Reglas de negocio

### RN-01. Acceso autorizado

Solo un usuario autenticado y autorizado puede consultar las ubicaciones de una persona monitoreada.

### RN-02. Asociación válida

Una persona monitoreada y su dispositivo deben estar asociados conforme a las relaciones y permisos definidos por el sistema.

### RN-03. Ubicación válida

El sistema debe rechazar coordenadas que estén fuera de los rangos geográficos válidos o que no cumplan las validaciones establecidas.

### RN-04. Registro temporal

Cada ubicación almacenada debe contar con la fecha y hora necesarias para identificar su antigüedad y ordenar el historial.

### RN-05. Historial de 72 horas

La consulta del historial del MVP debe limitarse al periodo de las últimas 72 horas, calculado respecto al momento de la consulta.

### RN-06. Salida de zona segura

Una alerta de salida debe generarse cuando una ubicación válida indique que la persona ha salido de la zona segura, conforme a la lógica de evaluación definida.

### RN-07. Ubicación desactualizada

Una ubicación no debe presentarse como actual cuando haya superado el tiempo máximo de actualización establecido por el sistema.

### RN-08. Protección de contraseñas

Las contraseñas no deben almacenarse ni mostrarse en texto plano.

### RN-09. Protección de datos

Los datos personales y las ubicaciones deben utilizarse únicamente para los fines autorizados y deben estar protegidos contra consultas no permitidas.

### RN-10. Estado de dispositivo desconocido

Si el sistema no recibe información suficiente para determinar el estado de un dispositivo, debe indicar que el dato no está disponible, en lugar de asumir que el dispositivo funciona correctamente.

### RN-11. Notificaciones repetidas

El sistema debe controlar la generación de alertas repetidas para un mismo evento, según las reglas de negocio que se definan.

### RN-12. Suscripciones y pagos

Las restricciones por mora o vencimiento de una suscripción solo deberán aplicarse cuando se implemente y valide el módulo correspondiente. No deben bloquear funcionalidades del MVP de forma improvisada.

## 10. Criterios generales de aceptación

El MVP se considerará funcional cuando:

- El backend se conecte correctamente a la base de datos.
- Las operaciones de usuario incluidas en el alcance funcionen y estén probadas.
- Los usuarios puedan acceder únicamente a la información autorizada.
- Se puedan registrar y consultar ubicaciones recibidas desde un dispositivo autorizado.
- Se pueda consultar la última ubicación y su fecha de registro.
- Se puedan configurar zonas seguras.
- Se generen alertas para los eventos implementados y probados.
- El historial permita consultar las últimas 72 horas.
- Los errores se gestionen sin exponer credenciales ni información sensible.
- La documentación refleje las funcionalidades realmente implementadas.

## 11. Restricciones y consideraciones

- El proyecto utiliza FastAPI, SQLAlchemy y MySQL en el backend actual.
- La aplicación web existente debe aprovecharse y evolucionar de forma incremental.
- La captura de ubicación depende de los permisos concedidos al dispositivo y de la disponibilidad del GPS.
- Si el teléfono está apagado, no tiene conexión o no puede obtener coordenadas, el sistema no puede garantizar una ubicación nueva en tiempo real.
- El historial depende de que las ubicaciones se hayan registrado correctamente.
- La estructura real de MySQL debe contrastarse con los modelos del backend antes de realizar cambios en el esquema.
- Las funcionalidades deben probarse antes de considerarse terminadas.

## 12. Evolución futura

Después de validar el MVP, se podrán evaluar:

- Integración con dispositivos GPS dedicados.
- Notificaciones mediante servicios externos.
- Gestión de suscripciones y pagos.
- Aplicaciones móviles nativas.
- Reportes y estadísticas de desplazamiento.
- Mejoras de escalabilidad y despliegue.

Cada nueva funcionalidad debe analizarse, documentarse y priorizarse antes de incorporarse al desarrollo.
