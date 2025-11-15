# SumiMetalicos-S.A
Proyecto de software para que la compañía SumiMetalicos S.A pueda generar informes en formato PDF acerca de sus clientes y de las estadísticas de venta de la propia empresa. Y si lo pide también podemos desarrollar nuevas plantillas de informes para los datos que se soliciten de la BD.  

## Requisitos para su ejecución
- JVM (Java Virtual Machine)
- Linux (SO compatible para la generación de informes por la configuración de rutas en el código del controlador "**crearinforme.py**")

## Tecnologías utilizadas
Lenguaje de Programación: **Python**  
Entornos de Desarrollo: **Eclipse IDE** (con plugin **PyDev**)  
Patrón de Diseño y Arquitectura: **MVC**  

Base de Datos: **SQLite** (también se aloja un fichero SQL para generar la BD en MySQL)  
Frameworks: **PySide6** (GUI de Escritorio)  

Diseño de Informes: **Jaspersoft Studio** (Community Edition)  
Librerías: **pyreportjasper**  

## Ventana Principal
1º) Para usar el software una vez ejecutado, primero hay que seleccionar la carpeta donde están todos las plantillas de informes JRXML para seleccionar uno de ellos para generar un PDF basado en los datos obtenidos de la BD correspondientes.  

2º) Una vez seleccionada la ruta donde se encuentran las plantillas de informes JRXML hay que seleccionar la ruta en la que se desea generar un PDF de la plantilla de informe seleccionada.  

3º) Finalmente, hay que seleccionar uno de los informes a generar pulsando el botón correspondiente y si piden parámetros los introducimos (ej. ID del cliente o pedido).  

<img width="527" height="452" alt="Captura de pantalla 2025-11-15 134614" src="https://github.com/user-attachments/assets/342481e1-032c-4554-b1b2-140343a72105" />
