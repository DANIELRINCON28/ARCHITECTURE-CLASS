# cine/serializers.py
from rest_framework import serializers
from .models import Pelicula, Usuario, Reserva

# La capa de "traducción". Convierte los objetos de Python a JSON y viceversa.

# Principio de Responsabilidad Única (SRP): Cada serializador tiene la única responsabilidad
# de convertir los datos de un modelo específico a un formato como JSON.
# Separación de Responsabilidades (SoC): Este archivo se ocupa únicamente de la "presentación" de los datos,
# separando esta lógica del modelo y de la vista.
class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__' # Incluye todos los campos

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email']

# Serializer para mostrar las reservas de forma legible
class ReservaSerializer(serializers.ModelSerializer):
    # StringRelatedField muestra el nombre del usuario/película en lugar del ID.
    usuario = serializers.StringRelatedField()
    pelicula = serializers.StringRelatedField()

    class Meta:
        model = Reserva
        fields = ['id', 'usuario', 'pelicula', 'fecha_reserva']

# Serializer específico para crear una reserva (recibe los IDs)
class CrearReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['usuario', 'pelicula']