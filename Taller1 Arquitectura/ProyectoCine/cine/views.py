# cine/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Pelicula, Usuario, Reserva
from .serializers import (
    PeliculaSerializer, 
    UsuarioSerializer, 
    ReservaSerializer, 
    CrearReservaSerializer
)
from rest_framework import viewsets

# Esta es la capa de Lógica (El "Controlador" en MVC)
# Maneja las peticiones del usuario y devuelve una respuesta.

# Separación de Responsabilidades (SoC): Este archivo actúa como el "controlador", manejando la lógica de las solicitudes HTTP.
# No te Repitas (DRY) y Mantenlo Simple (KISS): ModelViewSet genera automáticamente toda la lógica CRUD (Crear, Leer, Actualizar, Borrar).
# En lugar de escribir cientos de líneas, solo necesitamos definir el queryset y el serializer.
# Inversión de Dependencias (DIP): La vista depende de una abstracción (el ORM de Django, `Pelicula.objects.all()`)
# y no de una implementación de base de datos concreta.
class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ReservaListCreateView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    
    # Esta función decide qué serializer usar dependiendo de la acción (GET o POST)
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CrearReservaSerializer
        return ReservaSerializer