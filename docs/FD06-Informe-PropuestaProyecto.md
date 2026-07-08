![](images/FD01/FD01_01.png)


UNIVERSIDAD PRIVADA DE TACNA


FACULTAD DE INGENIERÍA


Escuela Profesional de Ingeniería de Sistemas



Proyecto Administrador de BD en consola o terminal


Curso: Base de Datos II



Docente: Patrick Cuadros Quiroga



Integrantes:


Jahuira Pilco, Dayan Elvis					(2022075749)

Mamani Cori, Cristhian Carlos				(2023077282)






Tacna – Perú

2026


---


**Proyecto**

**Administrador de BD en consola o terminal, Tacna, 2026**

Presentado por:

Dayan Jahuira Pilco — Estudiante de Ingeniería de Sistemas

Cristhian Mamani Cori — Estudiante de Ingeniería de Sistemas

06/07/2026


| CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES |
| --- | --- | --- | --- | --- | --- |
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| 1.0 | DJ - CM | PCQ | PCQ | 26/04/2026 | Versión Original |
| 2.0 | DJ - CM | PCQ | PCQ | 06/06/2026 | Versión 2.0 |
| 3.0 | DJ - CM | PCQ | PCQ | 06/07/2026 | Versión Final |


ÍNDICE GENERAL


# Propuesta narrativa

## Planteamiento del Problema

Las herramientas actuales de administración de bases de datos, en su mayoría, se presentan mediante interfaces gráficas que abstraen el funcionamiento interno de las operaciones, lo que limita la comprensión profunda de los procesos de manipulación de datos. En entornos profesionales y de servidores predomina el uso de interfaces de línea de comandos por su eficiencia y bajo consumo de recursos, aunque estas herramientas suelen presentar una curva de aprendizaje elevada. Adicionalmente, la mayoría de herramientas existentes se enfocan exclusivamente en bases de datos relacionales, dejando de lado los motores NoSQL, cuyo uso ha crecido de forma sostenida en aplicaciones modernas. En este contexto, se identifica la necesidad de desarrollar una solución que permita comprender y aplicar los conceptos de administración de bases de datos mediante una interfaz de consola simplificada y controlada.

## Justificación del proyecto

La inversión en el desarrollo del Administrador de BD en consola se justifica por la eliminación de la dependencia de herramientas gráficas comerciales, la reducción del tiempo de aprendizaje de comandos SQL mediante una interfaz simplificada, la automatización de tareas repetitivas de administración de bases de datos y la disponibilidad de una herramienta didáctica gratuita para la enseñanza de bases de datos. Asimismo, el proyecto aprovecha la oportunidad existente en el ámbito educativo de ofrecer una solución intermedia entre las interfaces gráficas comerciales y las herramientas profesionales de consola, ampliando el público alcanzable mediante su distribución en el Marketplace de Visual Studio Code, PyPI y Telegram, sin incurrir en costos de licenciamiento.

## Objetivo general

Desarrollar una aplicación en consola, denominada NexusDB, que permita administrar bases de datos relacionales (SQLite, PostgreSQL, MySQL) y no relacionales (MongoDB, Redis, Cassandra) mediante comandos estructurados, facilitando la ejecución de operaciones básicas de gestión de datos, así como la generación asistida de consultas SQL a partir de lenguaje natural.

## Beneficios

El desarrollo del proyecto genera los siguientes beneficios para el equipo desarrollador y los usuarios finales:

- Fortalecimiento de competencias técnicas del equipo desarrollador en Python, bases de datos y arquitectura de software.
- Contribución al aprendizaje práctico de la administración de bases de datos sin depender de interfaces gráficas.
- Disponibilidad del código fuente bajo licencia MIT para futuras adaptaciones e independencia de plataformas comerciales.
- Experiencia práctica en la integración con protocolos emergentes de inteligencia artificial (MCP) y en buenas prácticas de seguridad para bots conversacionales.
- Portafolio de distribución real (Marketplace de VS Code, PyPI y Telegram) que fortalece el perfil profesional de los integrantes.

## Alcance

El sistema permitirá administrar bases de datos relacionales y no relacionales mediante una interfaz de línea de comandos (CLI). Dentro del alcance del proyecto se considera:

- Conexión a seis gestores de bases de datos: PostgreSQL, MySQL y SQLite (relacionales), y MongoDB, Redis y Cassandra (NoSQL, en modo de consulta).
- Ejecución de comandos SQL directos (SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER) con visualización de resultados en formato tabular.
- Módulo de migración ETL entre distintos motores de base de datos, panel de rendimiento y comparador de esquemas.
- Generación de consultas SQL a partir de lenguaje natural mediante modelos de IA, y asistente de voz (NexusVoice).
- Distribución mediante extensión de Visual Studio Code (Marketplace), servidor MCP (PyPI) y bot de Telegram (solo lectura).

Quedan fuera del alcance el desarrollo de un motor de base de datos propio, la implementación de una interfaz gráfica de usuario y la administración de usuarios y permisos a nivel de SGBD.

## Requerimientos del sistema

Para el desarrollo y ejecución del sistema se requieren los siguientes recursos de hardware y software:

- Computadora personal con procesador Intel i5 o equivalente, 8 GB de RAM y 1 TB de almacenamiento.
- Sistema operativo Windows, Linux o macOS.
- Python 3.8 o superior, junto con las librerías de conexión psycopg2, mysql-connector-python, pymongo, redis y cassandra-driver.
- Node.js y TypeScript para el desarrollo y empaquetado de la extensión de Visual Studio Code.
- Servidor VPS (Contabo, Debian 13) para el despliegue permanente del bot de Telegram y de las bases de datos de prueba MySQL, MongoDB y Redis.

## Restricciones

El proyecto presenta las siguientes restricciones:

- El usuario debe contar con conocimientos básicos de SQL.
- Se requiere tener instalado previamente el motor de base de datos correspondiente.
- Las contraseñas se ingresan en texto plano por consola.
- El sistema no cuenta con interfaz gráfica; funciona exclusivamente por terminal.
- El plazo de desarrollo es de 4 meses por tratarse de un proyecto académico.
- Las integraciones externas (servidor MCP y bot de Telegram) solo permiten operaciones de lectura, sin excepción, por motivos de seguridad.

## Supuestos

Para la ejecución del proyecto se asumen las siguientes condiciones:

- El usuario cuenta con una base de datos previamente instalada y configurada.
- Las librerías de conexión necesarias se encuentran disponibles como software de código abierto.
- Se dispone de un entorno de ejecución adecuado, con acceso a internet para la instalación inicial de dependencias y la integración con los servicios de inteligencia artificial.
- Los servicios de terceros utilizados (APIs de modelos de IA, Marketplace de VS Code, PyPI y API de Telegram) mantienen su disponibilidad y políticas de publicación.

## Resultados esperados

Al finalizar el proyecto se espera obtener los siguientes resultados:

- Una aplicación CLI funcional con conexión a los seis motores de bases de datos soportados.
- Ejecución de operaciones CRUD con visualización de resultados en formato de tabla legible y manejo básico de errores.
- Módulos complementarios operativos: migración ETL, panel de rendimiento, comparador de esquemas y asistente de consultas mediante IA.
- Tres canales de distribución activos: extensión de Visual Studio Code, servidor MCP y bot de Telegram.
- Documentación técnica completa del sistema.

## Metodología de implementación

El proyecto se desarrolla siguiendo una metodología iterativa e incremental basada en las fases del Proceso Unificado (Inicio, Elaboración, Construcción y Transición). El desarrollo del sistema prioriza en primer lugar el bucle REPL básico (help, exit), la conexión a SQLite por su simplicidad, la ejecución de comandos SQL y la visualización de resultados en tabla. Posteriormente se incorpora la conexión a PostgreSQL y MySQL, los comandos adicionales (tables, disconnect, info, cls/clear), el soporte para motores NoSQL, el módulo de migración ETL, el asistente de generación de consultas mediante IA y, finalmente, los tres canales de distribución externa del sistema.

## Actores claves

En la siguiente tabla se presentan los actores claves del proyecto, junto con su descripción y sus responsabilidades principales:

| Nombre | Descripción | Responsabilidad |
| --- | --- | --- |
| Docente del curso | Evaluador y supervisor del proyecto (Patrick Cuadros Quiroga) | Definir los criterios de evaluación, revisar la documentación y validar la funcionalidad del sistema |
| Estudiantes desarrolladores | Equipo responsable del desarrollo del sistema (Dayan Jahuira y Cristhian Mamani) | Diseñar, implementar, probar y documentar el sistema según los requisitos establecidos |
| Estudiantes usuarios | Usuarios finales de la herramienta | Utilizar el sistema para practicar la administración de bases de datos y reportar observaciones |

## Papel y responsabilidades del personal

El equipo de trabajo está conformado por dos estudiantes de Ingeniería de Sistemas, cuyos roles y responsabilidades se detallan a continuación:

| Personal | Responsabilidad |
| --- | --- |
| Dayan Jahuira Pilco | Jefe de proyecto, Analista y Programador |
| Cristhian Mamani Cori | Analista y Programador |

## Plan de monitoreo y evaluación

El avance del proyecto se controla mediante actividades periódicas de monitoreo y evaluación, según se muestra en la siguiente tabla:

|  | Responsable | Regularmente | Fuentes | Objetivo |
| --- | --- | --- | --- | --- |
| Monitoreo | Jefe del proyecto | Semanalmente | Informes que ha elaborado el grupo del proyecto. | Proporciona toda información operativa y efectiva. |
| Evaluación | Grupo del proyecto | Mensualmente | Tener un seguimiento de los informes realizados. | Poner los términos claro del proyecto, obtener logros y cumplir las metas que se había planeado al inicio. |

## Cronograma del proyecto

El proyecto tiene una duración total de 4 meses, distribuidos en las cuatro fases que se detallan a continuación:

| Fases | Duración |
| --- | --- |
| Inicio | Del 09/03/2026 al 26/04/2026 |
| Elaboración | Del 27/04/2026 al 06/06/2026 |
| Construcción | Del 07/06/2026 al 28/06/2026 |
| Transición | Del 29/06/2026 al 06/07/2026 |

## Hitos de entregables

Los entregables del proyecto se organizan según las fases del cronograma, tal como se muestra en la siguiente tabla:

|  | Entregables | Actividades |
| --- | --- | --- |
| Inicio | Documento de factibilidad | Viabilidad del proyecto |
|  | Propuesta del proyecto |  |
|  | Visión del proyecto |  |
| Elaboración | Documento SRS | Descripción de casos de uso |
|  |  | Modelo E-R |
|  |  | Prototipo del sistema |
|  | Documento SAD | Diagrama de paquetes |
|  |  | Diagrama de clases |
|  |  | Diagrama de despliegue |
|  |  | Diagrama de componentes |
|  | Diccionario de Datos |  |
|  | Estándar de programación |  |
| Construcción | Implementación | Código (Elaboración de los casos de uso) |
| Transición | Manual de usuario |  |
|  | Pruebas del Sistema |  |

# Presupuesto

## Planteamiento de aplicación del presupuesto

El presupuesto del proyecto contempla los costos generales de equipamiento, los costos operativos durante el desarrollo, los costos del ambiente de trabajo y los costos del personal involucrado, calculados para una duración de 4 meses de desarrollo, conforme al detalle presentado en el Informe de Factibilidad (FD01).

## Presupuesto

El presupuesto total del proyecto asciende a S/. 18,420.00, distribuido en las siguientes categorías:

| Categoría | Total (S/.) |
| --- | --- |
| Costos Generales | S/. 5,040.00 |
| Costos Operativos | S/. 1,060.00 |
| Costos del Ambiente | S/. 320.00 |
| Costos de Personal | S/. 12,000.00 |
| **Total** | **S/. 18,420.00** |

## Análisis de Factibilidad

### Factibilidad Técnica

El proyecto es técnicamente viable: se cuenta con los equipos y herramientas necesarias para su desarrollo, tal como se detalla en la siguiente tabla:

| Tipo de Recurso | Nombre | Descripción |
| --- | --- | --- |
| Hardware | Equipo | Intel i5 |
|  |  | RAM 8 GB |
|  |  | Mouse: Estándar |
|  |  | Teclado: Estándar |
| Software | Windows 10 | Sistema Operativo |
|  | Aplicación | Python 3.8+ |
|  |  | Visual Studio Code |

### Factibilidad Económica

La inversión total del proyecto asciende a S/. 18,420.00. Los indicadores financieros calculados en el Informe de Factibilidad (VAN de S/. 3,373.27, TIR de 21.9% y relación Beneficio/Costo de 1.18) confirman que el proyecto es económicamente viable.

### Factibilidad Operativa

El sistema resulta operativamente viable: los usuarios objetivo (estudiantes, docentes y desarrolladores) cuentan con el perfil adecuado, la curva de aprendizaje es baja gracias al comando help y a la sintaxis intuitiva, y el mantenimiento se facilita por el diseño modular del código. Adicionalmente, la distribución mediante la extensión de VS Code, el servidor MCP y el bot de Telegram amplía el alcance operativo a usuarios que no utilizan la terminal como interfaz principal.

## Evaluación Financiera

La evaluación financiera del proyecto, considerando una tasa de descuento del 12%, arroja los siguientes indicadores:

- Valor Actual Neto (VAN): S/. 3,373.27; al ser mayor a 0, el proyecto genera valor por encima de lo necesario para recuperar la inversión.
- Tasa Interna de Retorno (TIR): 21.9%, superior a la tasa de descuento del 12%.
- Relación Beneficio/Costo (B/C): 1.18; por cada sol invertido, el proyecto genera S/. 1.18 en beneficios actualizados.

En consecuencia, todos los indicadores superan los criterios mínimos establecidos, por lo que el proyecto es rentable y financieramente viable.


---


## Anexo 01 – Requerimientos del Sistema *NexusDB – Administrador de BD en consola o terminal*

### RESUMEN EJECUTIVO

| | |
| --- | --- |
| **Nombre del Proyecto propuesto:** | *Administrador de BD en consola o terminal (NexusDB), Tacna, 2026* |
| **Propósito del Proyecto y Resultados esperados:** | El propósito del proyecto es *desarrollar una aplicación de consola, denominada NexusDB, que permita administrar bases de datos relacionales y no relacionales de forma segura, eficiente y educativa, integrando además capacidades de inteligencia artificial y distribución multicanal*. Los resultados esperados son: *una herramienta CLI funcional (NexusDB) compatible con seis motores de bases de datos (SQLite, PostgreSQL, MySQL, MongoDB, Redis y Cassandra), distribuida mediante una extensión de Visual Studio Code, un servidor MCP y un bot de Telegram*. |
| **Población Objetivo:** | Estudiantes, docentes y desarrolladores de la Escuela Profesional de Ingeniería de Sistemas de la Universidad Privada de Tacna |
| **Monto de Inversión (En Soles):** | **S/. 18,420.00** |
| **Duración del Proyecto (En Meses):** | **4 meses** |
