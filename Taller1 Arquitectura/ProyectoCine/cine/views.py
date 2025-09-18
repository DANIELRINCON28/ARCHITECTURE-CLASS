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

# Esta es la capa de Lógica (El "Controlador" en MVC)
# Maneja las peticiones del usuario y devuelve una respuesta.

class PeliculaListCreateView(generics.ListCreateAPIView):
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