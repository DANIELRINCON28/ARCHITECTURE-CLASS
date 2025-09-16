A continuación se detalla cómo el proyecto ProyectoCine (Django) corrige las malas prácticas identificadas en el script ejercicio.php, aplicando principios de arquitectura de software.

1. Encapsulamiento

Problema en ejercicio.php: Los datos ($usuarios, $peliculas) eran públicos, permitiendo su modificación directa desde fuera de la clase, lo que es riesgoso.

Solución en ProyectoCine: Se utiliza el ORM de Django en cine/models.py. Las clases como Pelicula definen los campos de datos, pero la lógica para acceder y manipular la base de datos está encapsulada dentro del framework. No interactúas directamente con la base de datos, sino con los objetos del modelo, protegiendo la integridad de los datos.


2. Separación de Responsabilidades (SoC) y Cohesión

Problema en ejercicio.php: La clase Cine era una "clase Dios" que hacía todo: gestionaba usuarios, películas y reservas. Esto viola la cohesión y la separación de responsabilidades.

Solución en ProyectoCine: El proyecto está dividido en componentes con responsabilidades únicas:
models.py: Define la estructura de los datos (el Modelo).
views.py: Maneja la lógica de las solicitudes HTTP (el Controlador).

serializers.py: Controla cómo se presentan los datos en formato JSON (la Vista/Presentación).
urls.py: Gestiona el enrutamiento de las URLs. Esta estructura garantiza que cada parte del sistema tenga una única responsabilidad (alta cohesión).


3. Principio de Responsabilidad Única (SRP - de SOLID)

Problema en ejercicio.php: La clase Cine violaba directamente este principio al tener múltiples razones para cambiar (cambios en la lógica de usuarios, películas o reservas).

Solución en ProyectoCine: Cada clase tiene una única responsabilidad. La clase Pelicula en models.py solo se ocupa de la estructura de una película. La clase PeliculaViewSet en views.py solo se ocupa de las operaciones (CRUD) para las películas.


4. Principio de Abierto/Cerrado (OCP - de SOLID)

Problema en ejercicio.php: Para añadir el detalle de una nueva película, había que modificar el método mostrarDetallePelicula con un nuevo if/else. El código no estaba cerrado a modificaciones.

Solución en ProyectoCine: El sistema es extensible sin necesidad de modificar el código existente. Para añadir una nueva entidad (ej. Promocion), simplemente creas un nuevo modelo, serializador y vista. No necesitas tocar el código de Pelicula. El sistema está abierto a la extensión, pero cerrado a la modificación.


5. Inversión de Dependencias (DIP - de SOLID)

Problema en ejercicio.php: La clase Cine dependía de una implementación concreta (arrays de PHP) para almacenar los datos.

Solución en ProyectoCine: Las vistas (views.py) no dependen de una base de datos específica (SQLite, PostgreSQL), sino de una abstracción: el ORM de Django. Esto permite cambiar el motor de la base de datos en settings.py sin tener que cambiar una sola línea de código en las vistas o modelos.


6. No te Repitas (DRY - Don't Repeat Yourself)

Problema en ejercicio.php: La validación de email estaba duplicada.

Solución en ProyectoCine: Django Rest Framework (DRF) y Django promueven DRY de forma masiva. Por ejemplo, en views.py, en lugar de escribir la lógica para crear, leer, actualizar y borrar para cada modelo, ModelViewSet lo hace automáticamente. El router en urls.py también genera todas las URLs necesarias para el CRUD sin que tengas que escribirlas una por una.


7. Mantenlo Simple (KISS - Keep It Simple, Stupid)

Problema en ejercicio.php: La cadena de if/else para los detalles de las películas era innecesariamente complicada.
Solución en ProyectoCine: El código es declarativo y simple. En views.py, un ViewSet se define con solo dos líneas (queryset y serializer_class), y el framework se encarga de toda la complejidad. La lógica es fácil de leer y entender.

# Comentarios en el Código
He añadido comentarios directamente en los archivos models.py, serializers.py, views.py y urls.py de tu proyecto ProyectoCine para que puedas identificar dónde y cómo se aplican estos principios en la práctica.
