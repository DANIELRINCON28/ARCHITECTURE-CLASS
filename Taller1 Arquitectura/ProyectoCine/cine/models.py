# cine/models.py
from django.db import models

# Esta es la capa de datos (El "Modelo" en MVC/MVT)
# Cada clase representa una tabla en la base de datos.

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

class Reserva(models.Model):
    # ForeignKey crea una relación. 'on_delete=models.CASCADE' significa que
    # si se borra un usuario o película, sus reservas también se borrarán.
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    # auto_now_add=True guarda la fecha y hora automáticamente al crear la reserva.
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reserva de {self.usuario.nombre} para {self.pelicula.titulo}'