![](images/FD02/FD02_01.png)


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



| CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES |
| --- | --- | --- | --- | --- | --- |
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| 1.0 | DJ - CM | PCQ | PCQ | 26/04/2026 | Versión Original |
| 2.0 | DJ - CM | PCQ | PCQ | 06/06/2026 | Versión 2.0 |
| 3.0 | DJ - CM | PCQ | PCQ | 06/07/2026 | Versión Final |













# Sistema Administrador de BD en consola o terminal

# Documento de Visión


# Versión 3.0


| CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES | CONTROL DE VERSIONES |
| --- | --- | --- | --- | --- | --- |
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| 1.0 | DJ - CM | PCQ | PCQ | 26/04/2026 | Versión Original |
| 2.0 | DJ - CM | PCQ | PCQ | 06/06/2026 | Versión 2.0 |
| 3.0 | DJ - CM | PCQ | PCQ | 06/07/2026 | Versión Final |



INDICE GENERAL



Informe de Visión

# Introducción

## Propósito

El presente documento tiene como propósito definir la visión general del sistema “Administrador de Base de Datos en Consola”, estableciendo sus objetivos, alcance, características principales y los actores involucrados. Sirve como guía para el desarrollo del proyecto y como base para la toma de decisiones durante su implementación.

## Alcance

El sistema permitirá administrar bases de datos relacionales y no relacionales mediante una interfaz de línea de comandos (CLI), ejecutando operaciones como creación de tablas, manipulación de datos (operaciones CRUD) y consultas SQL personalizadas. El sistema se integrará con seis gestores de bases de datos ampliamente utilizados: PostgreSQL, MySQL y SQLite (relacionales), y MongoDB, Redis y Cassandra (NoSQL). Adicionalmente, se distribuirá mediante una extensión de Visual Studio Code, un servidor MCP (Model Context Protocol) y un bot de Telegram en modo de solo lectura.

Dentro del alcance:

- Conexión a bases de datos existentes mediante parámetros de configuración.

- Ejecución de comandos SQL directos (SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER).

- Visualización de resultados en formato tabular legible dentro de la consola.

- Listado de tablas disponibles en la base de datos conectada.

- Manejo básico de errores de sintaxis y conexión.

- Comando de ayuda integrado (help) para consultar instrucciones disponibles.

Comando para salir del programa (exit).

- Conexión y consultas de solo lectura sobre motores NoSQL: MongoDB (find), Redis (comandos de lectura) y Cassandra (CQL).

- Generación de consultas SQL a partir de lenguaje natural mediante IA (con respaldo por patrones si no hay clave de IA configurada).

- Distribución del sistema mediante extensión de VS Code (Marketplace), servidor MCP (PyPI) y bot de Telegram (solo lectura).

Fuera del alcance:

- Desarrollo de un motor de base de datos propio.

- Interfaz gráfica de usuario (GUI).

- Administración de usuarios y permisos a nivel de SGBD.

- Generación de reportes o exportación a otros formatos (CSV, Excel, PDF).

- Conexión simultánea a múltiples bases de datos.

- Funcionalidades de respaldo (backup) o restauración automatizada.

- Operaciones de escritura (INSERT, UPDATE, DELETE, DROP, etc.) desde las integraciones externas: el servidor MCP y el bot de Telegram solo permiten consultas de lectura por motivos de seguridad.

## Definiciones, Siglas y Abreviaturas


## Referencias

- Documentación oficial de Python 3.8+

- Documentación oficial de PostgreSQL 13+

- Documentación oficial de MySQL 8.0+

- Documentación oficial de SQLite 3

- Informe de Factibilidad del proyecto (FD01) – Versión 1.0

## Visión General

La visión del proyecto es desarrollar una herramienta de administración de bases de datos basada en consola que permita a los usuarios interactuar de manera directa, eficiente y controlada con un sistema gestor de bases de datos, sin depender de interfaces gráficas que abstraen los procesos internos.

El sistema busca ofrecer una experiencia simplificada pero funcional, enfocada en la ejecución de comandos SQL directos y estructurados, permitiendo realizar operaciones fundamentales de definición y manipulación de datos. A través de esta interacción, se pretende reforzar la comprensión de los procesos internos de gestión de datos y el uso práctico del lenguaje SQL.

Asimismo, la solución se orienta a un contexto educativo y técnico, donde la prioridad no es competir con herramientas profesionales existentes (como DBeaver, Navicat o pgAdmin), sino proporcionar un entorno controlado que facilite el aprendizaje progresivo de la administración de bases de datos y el desarrollo de aplicaciones basadas en comandos.

La herramienta será compatible con tres sistemas gestores de bases de datos: PostgreSQL, MySQL y SQLite, permitiendo su aplicación en distintos entornos de desarrollo, desde bases de datos ligeras de archivo (SQLite) hasta servidores de producción (PostgreSQL/MySQL).

# Posicionamiento

## Oportunidad de negocio

Existe una oportunidad significativa en el ámbito educativo y formativo para desarrollar herramientas que permitan a los estudiantes comprender el funcionamiento interno de las bases de datos sin depender de interfaces gráficas. La mayoría de las herramientas comerciales y de código abierto actuales priorizan la facilidad de uso mediante interfaces visuales, lo que, si bien es útil en entornos productivos, limita la comprensión técnica de los procesos subyacentes.

En el entorno profesional, el uso de interfaces de línea de comandos es predominante en servidores y entornos de automatización, donde la eficiencia, el bajo consumo de recursos y la capacidad de scripting son valorados. Sin embargo, estas herramientas profesionales presentan una curva de aprendizaje elevada.

El proyecto aprovecha esta brecha ofreciendo una solución intermedia: una CLI simplificada, didáctica y funcional, que permite aprender y administrar bases de datos sin las complejidades de herramientas como psql (PostgreSQL) o mysql (cliente MySQL), pero conservando la esencia de la interacción por comandos.

## Definición del problema

Las herramientas actuales de administración de bases de datos suelen abstraer los procesos internos mediante interfaces gráficas, limitando la comprensión técnica. Además, en entornos sin interfaz gráfica, el uso de herramientas de consola puede resultar complejo para usuarios no experimentados.

# Descripción de los interesados y usuarios

## Resumen de los interesados


## Resumen de los usuarios


## Entorno de usuario

El sistema será utilizado en entornos de desarrollo local, mediante terminal o consola, en sistemas operativos como Windows (CMD, PowerShell, Windows Terminal), Linux (Bash, Zsh) o macOS (Terminal, iTerm2). No se requiere conexión a internet para su funcionamiento básico, salvo para la instalación inicial de dependencias.

## Perfiles de los interesados


## Perfiles de los Usuarios


## Necesidades de los interesados y usuarios


# Vista General del Producto

## Perspectiva del producto

El sistema es una aplicación independiente desarrollada en Python 3.8+ que actúa como intermediario entre el usuario y el sistema gestor de base de datos. No reemplaza al SGBD, sino que se conecta a uno existente, interpreta los comandos ingresados por el usuario (que pueden ser SQL directo o comandos internos del sistema) y ejecuta las operaciones correspondientes.

## Resumen de capacidades

- Conexión a bases de datos

- Ejecución de comandos SQL

- Gestión de tablas

- Operaciones CRUD

- Visualización de resultados en consola

## Suposiciones y dependencias

- El usuario cuenta con una base de datos previamente instalada

- Disponibilidad de librerías de conexión en Python

- Acceso a un entorno de ejecución adecuado

## Costos y precios

El proyecto se desarrolla con fines académicos y no tiene un modelo de negocio asociado. Sin embargo, para efectos de simulación profesional, se presentan los costos estimados de desarrollo y los precios de referencia si el producto fuera comercializado.

Costos de desarrollo (tomados del informe de factibilidad FD01):


## Licenciamiento e instalación

El proyecto utiliza Licencia MIT, que permite el uso, copia, modificación, fusión, publicación, distribución, sublicencia y venta del software, siempre que se incluya el aviso de copyright y la licencia en las distribuciones. Esta licencia es compatible con el uso académico y comercial.

# Características del producto

MUST (Indispensables)

- Conexión a bases de datos (PostgreSQL, MySQL, SQLite).

- Ejecución de comandos SQL (SELECT, INSERT, UPDATE, DELETE).

- Visualización de resultados en formato tabla.

- Comando de ayuda (help).

- Comando para salir (exit).

- Manejo básico de errores.

SHOULD (Importantes)

- Listado de tablas de la base de datos (tables).

- Información de la conexión activa (info).

- Desconexión de la base de datos (disconnect).

- Limpiar pantalla (cls / clear).

- Conexión y consultas de lectura sobre MongoDB, Redis y Cassandra.

COULD (Opcionales)

- Ayuda específica por comando (help connect).

- Historial de comandos entre sesiones.

- Exportación de resultados a CSV.

- Generación de consultas SQL a partir de lenguaje natural mediante IA (comando preguntar).

- Distribución mediante extensión de VS Code, servidor MCP y bot de Telegram.

# Restricciones

- El usuario debe tener conocimientos básicos de SQL.

- Se requiere tener instalado previamente el motor de base de datos (PostgreSQL, MySQL o SQLite).

- Las contraseñas se ingresan en texto plano por consola.

- El sistema no cuenta con interfaz gráfica, solo funciona por terminal.

- Dependencia de librerías externas de Python.

- Plazo de desarrollo de 4 meses por ser proyecto académico.

- Las integraciones externas (MCP y Telegram) solo permiten operaciones de lectura, sin excepción.

# Rangos de calidad

- Usabilidad: Usuario nuevo logra conectarse en menos de 2 minutos usando el comando help.

- Confiabilidad: Tasa de fallos en comandos SQL válidos menor al 1%.

- Rendimiento: Respuesta menor a 1 segundo para consultas simples.

- Portabilidad: Funciona en Windows, Linux y macOS con Python 3.8+.

- Robustez: El sistema no colapsa ante errores, permite seguir ingresando comandos.

# Precedencia y Prioridad

Orden recomendado de desarrollo:

- Bucle REPL básico (help, exit)

- Conexión a SQLite (más simple, sin servidor)

- Ejecución de comandos SQL

- Visualización de resultados en tabla

- Conexión a PostgreSQL

- Conexión a MySQL

- Comando tables

- Comando disconnect

- Comando info

- Comando cls / clear

# Otros requerimientos del producto

- Estandares legales

El desarrollo del proyecto debe cumplir con las siguientes normas:

- Propiedad intelectual: El código desarrollado es propiedad de los autores. Se utilizará licencia MIT para permitir uso académico y libre distribución.

- Software de código abierto: Todas las librerías utilizadas (Python, mysql-connector, psycopg2, pymongo, redis, cassandra-driver, prompt_toolkit, python-telegram-bot, mcp) son de código abierto con licencias permisivas, sin necesidad de pago por su uso. La publicación en Visual Studio Code Marketplace, PyPI y la API de Bots de Telegram se realiza conforme a los acuerdos de publicación de cada plataforma, sin costo asociado.

- Protección de datos: El sistema no almacena ni procesa datos personales de los usuarios, solo actúa como interfaz para consultar bases de datos externas

- Estandares de comunicación

- Los mensajes del sistema utilizan iconos claros: ✅ para éxito, ❌ para error, ℹ️ para información.

- El comando help muestra todos los comandos disponibles de forma organizada.

- Los resultados de consultas se muestran en formato de tabla con bordes ASCII.

- Los errores se muestran con mensajes descriptivos y en español, sin mostrar código técnico interno.

- Estandaraes de cumplimiento de la plataforma

- Multiplataforma: El sistema funciona en Windows, Linux y macOS sin modificaciones.

- Terminal: Compatible con cualquier terminal estándar (CMD, PowerShell, Bash, Zsh).

- Python: Requiere Python 3.8 o superior instalado en el sistema.

- Dependencias: Se incluye archivo requirements.txt para instalar todas las librerías necesarias.

- Estandaraes de calidad y seguridad

Calidad:

- Código modular y documentado con docstrings.

- Seguimiento de las convenciones PEP 8 de Python.

- Manejo de errores para evitar que el programa colapse.

- Interfaz de consola clara y fácil de usar.

Seguridad:

- Las credenciales no se almacenan en archivos ni logs.

- Las conexiones se cierran explícitamente al salir o usar disconnect.

- Validación básica de comandos internos.

- No se concatenan parámetros del usuario en consultas internas (como la de listar tablas).

- El servidor MCP y el bot de Telegram validan cada comando contra un patrón de solo lectura antes de ejecutarlo, rechazando cualquier operación de escritura.

# CONCLUSIONES

El proyecto Administrador de BD en consola o terminal es una solución viable que permite a los usuarios interactuar con bases de datos mediante comandos SQL desde una interfaz de línea de comandos.

El sistema cumple con los objetivos planteados: permite conectarse a PostgreSQL, MySQL y SQLite, ejecutar operaciones CRUD, mostrar resultados en formato tabla y manejar errores básicos.

El análisis de factibilidad confirma que el proyecto es viable desde las perspectivas técnica, económica, operativa, legal, social y ambiental.

La herramienta tiene un alto valor educativo, ya que permite a los estudiantes comprender el funcionamiento interno de las bases de datos sin depender de interfaces gráficas.

El código desarrollado es modular y extensible, lo que facilita su mantenimiento y la incorporación de nuevas funcionalidades en el futuro.

# RECOMENDACIONES

Realizar pruebas con cada uno de los tres motores de base de datos soportados antes de la presentación.

Preparar un script de demostración que muestre una conexión exitosa, una consulta SELECT con varias filas y un ejemplo de manejo de errores.

Verificar que la terminal utilizada durante la presentación soporte caracteres Unicode para que las tablas se muestren correctamente.

Incluir instrucciones claras de instalación y uso en un archivo README.

Para versiones futuras, implementar enmascaramiento de contraseñas usando el módulo getpass de Python.

# BIBLIOGRAFIA

Ramakrishnan, R., & Gehrke, J. (2003). Sistemas de Gestión de Bases de Datos (3ª ed.). McGraw-Hill.

Silberschatz, A., Korth, H. F., & Sudarshan, S. (2019). Database System Concepts (7ª ed.). McGraw-Hill Education.

Beaulieu, A. (2020). Learning SQL (3ª ed.). O'Reilly Media.

Python Software Foundation. (2026). The Python Standard Library.

# WEBGRAFIA

Python.org. (2026). *Python 3.8+ Documentation*. Recuperado de https://docs.python.org/3/

PostgreSQL Global Development Group. (2026). PostgreSQL Documentation. Recuperado de https://www.postgresql.org/docs/

Oracle Corporation. (2026). MySQL Documentation. Recuperado de https://dev.mysql.com/doc/

SQLite Consortium. (2026). SQLite Documentation. Recuperado de https://www.sqlite.org/docs.html

