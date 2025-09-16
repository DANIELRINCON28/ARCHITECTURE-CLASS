# cine/models.py
from django.db import models

# Esta es la capa de datos (El "Modelo" en MVC/MVT)
# Cada clase representa una tabla en la base de datos.

# Principio de Responsabilidad Única (SRP): Cada clase representa una única entidad de negocio.
# Encapsulamiento: El ORM de Django encapsula la lógica de acceso a la base de datos.
# Principio de Abierto/Cerrado (OCP): Para añadir un nuevo campo, solo se modifica este modelo,
# y para una nueva entidad, se crea una nueva clase sin tocar las existentes.
class Pelicula(models.Model):
    # CharField es para texto. `unique=True` asegura que no haya películas repetidas.
    titulo = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    # EmailField valida automáticamente que el formato sea de un correo.
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Sala(models.Model):
    # CharField es para texto. `unique=True` asegura que no haya salas repetidas.
    nombre = models.CharField(max_length=100, unique=True)
    capacidad = models.IntegerField()  # IntegerField es para números enteros.

    def __str__(self):
        return self.nombre

class Funcion(models.Model):
    # ForeignKey crea una relación. 'on_delete=models.CASCADE' significa que
    # si se borra una película, sus funciones también se borrarán.
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    # DateTimeField es para fechas y horas.
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f'Función de {self.pelicula.titulo} en {self.sala.nombre}'

class Cliente(models.Model):
    # CharField es para texto. `unique=True` asegura que no haya clientes repetidos.
    nombre = models.CharField(max_length=100, unique=True)
    # EmailField valida automáticamente que el formato sea de un correo.
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=15, unique=True)  # Para números de teléfono.

    def __str__(self):
        return self.nombre

class Asiento(models.Model):
    # ForeignKey crea una relación. 'on_delete=models.CASCADE' significa que
    # si se borra una sala, los asientos asociados también se borrarán.
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    fila = models.CharField(max_length=1)  # Letra de la fila.
    numero = models.IntegerField()  # Número del asiento en la fila.

    class Meta:
        unique_together = ('sala', 'fila', 'numero')  # Combinación única de sala, fila y número.

    def __str__(self):
        return f'Asiento {self.numero} en fila {self.fila} - Sala {self.sala.nombre}'

class Reserva(models.Model):
    # ForeignKey crea una relación. 'on_delete=models.CASCADE' significa que
    # si se borra un usuario o película, sus reservas también se borrarán.
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    # auto_now_add=True guarda la fecha y hora automáticamente al crear la reserva.
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reserva de {self.usuario.nombre} para {self.pelicula.titulo}'

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Para precios con decimales.

    def __str__(self):
        return self.nombre

class Combo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    # ManyToManyField es para relaciones de muchos a muchos.
    productos = models.ManyToManyField(Producto)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)  # Porcentaje de descuento.

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    # ForeignKey crea una relación. 'on_delete=models.CASCADE' significa que
    # si se borra un usuario, sus compras también se borrarán.
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # ManyToManyField es para relaciones de muchos a muchos.
    productos = models.ManyToManyField(Producto)
    fecha_compra = models.DateTimeField(auto_now_add=True)  # Fecha y hora de la compra.

    def __str__(self):
        return f'Compra de {self.usuario.nombre} en {self.fecha_compra}'