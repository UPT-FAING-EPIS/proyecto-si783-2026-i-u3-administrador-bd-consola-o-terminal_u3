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














# Sistema Administrador de BD en consola o terminal

# Informe de Factibilidad


# Versión {1.0}
















| CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES |
| --- | --- | --- | --- | --- | --- |
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| 1.0 | DJ - CM | PCQ | PCQ | 3/7/2026 | Versión Original |



ÍNDICE GENERAL




Informe de Factibilidad

# Descripción del Proyecto

## Nombre del proyecto

Administrador de BD en consola o terminal

## Duración del proyecto

4 meses

## Descripción

El presente proyecto tiene como finalidad el desarrollo de una aplicación de tipo CLI (Command Line Interface) orientada a la administración de bases de datos tanto relacionales como no relacionales. El sistema, denominado NexusDB, permitirá a los usuarios interactuar con gestores de base de datos relacionales (SQLite, PostgreSQL, MySQL) y no relacionales (MongoDB, Redis, Cassandra), mediante comandos estructurados definidos por la aplicación, así como mediante un módulo de generación asistida de consultas SQL a partir de lenguaje natural, apoyado en modelos de lenguaje (IA).

La herramienta será capaz de procesar instrucciones ingresadas por el usuario, interpretarlas mediante un módulo de análisis sintáctico y ejecutarlas sobre la base de datos, permitiendo operaciones de definición y manipulación de datos (DDL y DML) tanto en motores SQL como en sus equivalentes NoSQL. Asimismo, el sistema proporcionará mecanismos básicos de validación, control de errores, auditoría de comandos y visualización de resultados en formato legible dentro del entorno de consola. El proyecto incluye además un módulo de migración ETL entre distintos motores de base de datos, un panel de rendimiento, un comparador de esquemas, un asistente de voz (NexusVoice) y un módulo de gestión de usuarios con control de permisos.

Este proyecto se orienta tanto al aprendizaje práctico de la administración de bases de datos como al desarrollo de habilidades en el diseño de sistemas interactivos basados en comandos. Adicionalmente, el proyecto contempla la distribución del sistema mediante tres canales complementarios: una extensión para Visual Studio Code publicada en el Marketplace oficial, un servidor MCP (Model Context Protocol) publicado en el repositorio PyPI para su integración con asistentes de inteligencia artificial (Claude, Antigravity, Cursor, entre otros), y un bot de Telegram en modo de solo lectura para consultas remotas seguras. Con ello, se busca que el sistema no sea únicamente una herramienta de uso local, sino un producto de software distribuible y reutilizable por terceros.

## Objetivos

### Objetivo general

Desarrollar una aplicación en consola que permita administrar una base de datos mediante comandos, facilitando la ejecución de operaciones básicas de gestión de datos.

### Objetivos Específicos

- Implementar la conexión a una base de datos existente

- Desarrollar un sistema de comandos en consola (CLI)

- Permitir operaciones CRUD sobre las tablas

- Mostrar resultados de manera clara en consola

- Validar comandos y manejar errores básicos

- Incorporar soporte para motores de bases de datos no relacionales (MongoDB, Redis y Cassandra)

- Desarrollar un módulo de migración ETL que permita mover datos entre distintos motores de base de datos

- Integrar un asistente de generación de consultas SQL a partir de lenguaje natural mediante modelos de IA

- Distribuir el sistema como extensión de Visual Studio Code, servidor MCP y bot de Telegram

- Restringir las operaciones expuestas a integraciones externas (MCP y Telegram) a consultas de solo lectura, por motivos de seguridad

# Riesgos

- Falta de experiencia en conexión a bases de datos

- Problemas de configuración del entorno

- Errores en la interpretación de comandos

- Limitaciones de tiempo para completar todas las funcionalidades

- Fallas en la integración entre módulos

- Incompatibilidad de drivers o versiones entre los distintos motores NoSQL soportados

- Exposición accidental de credenciales de conexión en integraciones externas (bot de Telegram, servidor MCP)

- Indisponibilidad del servidor VPS donde se despliegan el bot de Telegram y las bases de datos de prueba

- Dependencia de servicios de terceros (APIs de modelos de IA, Marketplace de VS Code, PyPI, API de Telegram) que pueden cambiar sus políticas o interfaces

# Análisis de la Situación actual

## Planteamiento del problema

Las herramientas actuales de administración de bases de datos, en su mayoría, se presentan mediante interfaces gráficas que abstraen el funcionamiento interno de las operaciones, lo que limita la comprensión profunda de los procesos de manipulación de datos.

Por otro lado, en entornos profesionales y de servidores, el uso de interfaces de línea de comandos es predominante debido a su eficiencia, bajo consumo de recursos y capacidad de automatización. Sin embargo, dichas herramientas suelen presentar una curva de aprendizaje elevada.

En este contexto, se identifica la necesidad de desarrollar una solución que permita comprender y aplicar los conceptos de administración de bases de datos mediante una interfaz de consola simplificada y controlada.

Adicionalmente, se observa que la mayoría de herramientas existentes se enfocan exclusivamente en bases de datos relacionales, dejando de lado a los motores NoSQL, cuyo uso ha crecido de forma sostenida en aplicaciones modernas. Asimismo, la aparición de asistentes de inteligencia artificial capaces de operar herramientas externas mediante protocolos como MCP (Model Context Protocol) representa una oportunidad para modernizar la forma en que los desarrolladores interactúan con sus bases de datos, sin abandonar el control y la seguridad que ofrece una interfaz de consola tradicional.

## Consideraciones de hardware y software


# Estudio de Factibilidad

## Factibilidad Técnica

Conclusión Técnica: El proyecto es técnicamente viable. Se cuenta con dos equipos con especificaciones adecuadas para el desarrollo, además de un servidor VPS para el despliegue permanente de las integraciones externas. Python es un lenguaje ideal para aplicaciones CLI y no requiere hardware especializado. Las librerías necesarias para la conexión a bases de datos relacionales y NoSQL (psycopg2, mysql-connector-python, pymongo, redis, cassandra-driver) son de código abierto y están disponibles gratuitamente, al igual que las herramientas de publicación utilizadas (PyPI, Visual Studio Code Marketplace y la API de Bots de Telegram).

## Factibilidad Económica

### Costos Generales


### Costos operativos durante el desarrollo


### Costos del ambiente


### Costos de personal


### Costos totales del desarrollo del sistema


## Factibilidad Operativa


De acuerdo con el análisis presentado en la tabla, la factibilidad operativa del sistema resulta totalmente viable. Los usuarios objetivo tienen el perfil adecuado (conocimiento básico de bases de datos), el sistema incluye un comando de ayuda para facilitar su uso, y los riesgos identificados son controlables mediante una adecuada implementación de manejo de errores y documentación.

## Factibilidad Legal


## Factibilidad Social


## Factibilidad Ambiental


# Análisis Financiero

## Justificación de la Inversión

La inversión en el desarrollo del Administrador de BD en consola se justifica por los siguientes motivos:

- Eliminación de dependencia de herramientas gráficas comerciales como DBeaver Pro o Navicat

- Reducción del tiempo de aprendizaje para comandos SQL mediante una interfaz simplificada

- Automatización de tareas repetitivas de administración de bases de datos

- Disponibilidad de una herramienta didáctica gratuita para la enseñanza de bases de datos

- Cero costos en infraestructura por ser una aplicación 100% Python

- Ampliación del público alcanzable mediante distribución en el Marketplace de VS Code, PyPI y Telegram, sin costos de licenciamiento

- Reducción de la barrera de entrada al uso de bases de datos NoSQL mediante una sintaxis unificada con el motor relacional

### Beneficios del Proyecto

Beneficios Intangibles

- Fortalecimiento de competencias técnicas en el equipo desarrollador

- Contribución al aprendizaje práctico de bases de datos

- Disponibilidad de código fuente para futuras adaptaciones

- Independencia de plataformas comerciales

- Código ligero y portable al usar solo Python estándar

- Experiencia práctica del equipo en integración con protocolos emergentes de IA (MCP) y en buenas prácticas de seguridad para bots conversacionales

- Portafolio de distribución real (Marketplace, PyPI y Telegram) que fortalece el perfil profesional de los integrantes

### Criterios de Inversión

### Relación Beneficio/Costo (B/C)

B/C = Beneficios netos actualizados / Inversión inicial

B/C = (8,000/1.12 + 9,000/1.12² + 10,500/1.12³) / 18,420

B/C = 21,793.27 / 18,420 = 1.18

Interpretación: Como B/C es mayor a 1, por cada sol invertido el proyecto genera S/. 1.18 en beneficios actualizados, lo que indica que el proyecto es rentable.


### Valor Actual Neto (VAN)

VAN = -18,420 + 8,000 / (1.12)¹ + 9,000 / (1.12)² + 10,500 / (1.12)³

VAN = -18,420 + 7,142.86 + 7,175.51 + 7,474.90

VAN = S/. 3,373.27

Interpretación: VAN es mayor a 0, por lo tanto, el proyecto genera valor por encima de lo necesario para recuperar la inversión, considerando una tasa de descuento del 12%.

### Tasa Interna de Retorno (TIR)

La TIR se calcula como la tasa que hace el VAN igual a cero:

VAN = 0 = -11,370 + 4,100 / (1+TIR)¹ + 4,550 / (1+TIR)² + 5,000 / (1+TIR)³

Resolviendo la ecuación mediante interpolación:

Probando con tasa 21 por ciento:

VAN = -18,420 + 8,000/1.21 + 9,000/1.21² + 10,500/1.21³

VAN = -18,420 + 6,611.57 + 6,147.12 + 5,926.62 = 265.31

Probando con tasa 22 por ciento:

VAN = -18,420 + 8,000/1.22 + 9,000/1.22² + 10,500/1.22³

VAN = -18,420 + 6,557.38 + 6,047.03 + 5,783.36 = -32.23


# Conclusiones

El análisis de factibilidad realizado para el proyecto Administrador de BD en consola o terminal arroja los siguientes resultados:

Factibilidad Técnica: El proyecto es viable pues se cuenta con los conocimientos y herramientas necesarias para su desarrollo. Python con sus librerías estándar y de terceros permite construir una aplicación CLI completa con soporte SQL y NoSQL, integraciones de IA y distribución multicanal, sin requerir infraestructura costosa adicional más allá de un servidor VPS de bajo costo.

Factibilidad Económica: La inversión total asciende a S/. 18,420.00. Los indicadores financieros muestran resultados favorables con un VAN de S/. 3,373.27, una TIR de 21.9 por ciento y una relación Beneficio/Costo de 1.18, todos superiores a los criterios mínimos establecidos (VAN mayor a 0 y TIR mayor a la tasa de descuento del 12 por ciento).

Factibilidad Operativa: La interfaz de línea de comandos con comando help facilita la curva de aprendizaje. Los usuarios objetivo estudiantes y docentes cuentan con el perfil adecuado. Adicionalmente, la distribución mediante extensión de VS Code, servidor MCP y bot de Telegram amplía el alcance operativo a usuarios que no necesariamente usan la terminal como interfaz principal.

Factibilidad Legal: El proyecto utiliza exclusivamente software de código abierto con licencias permisivas, cumpliendo con las normativas de propiedad intelectual.

Factibilidad Social: El impacto es positivo al contribuir con la formación de los estudiantes y ofrecer una herramienta didáctica para la enseñanza de bases de datos.

Factibilidad Ambiental: El proyecto no genera residuos electrónicos ni consume recursos adicionales, promoviendo el uso de software libre.

