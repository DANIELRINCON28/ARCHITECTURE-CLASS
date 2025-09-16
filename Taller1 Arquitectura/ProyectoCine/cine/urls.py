# cine/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import PeliculaListCreateView, UsuarioListCreateView, ReservaListCreateView

# Separación de Responsabilidades (SoC): Este archivo se dedica únicamente a definir las rutas (URLs).
# No te Repitas (DRY): El DefaultRouter registra automáticamente todas las URLs necesarias para el CRUD
# de cada ViewSet, evitando tener que definir cada ruta (GET, POST, PUT, DELETE) manualmente.
router = routers.DefaultRouter()
router.register(r'peliculas', PeliculaListCreateView, basename='peliculas')
router.register(r'usuarios', UsuarioListCreateView, basename='usuarios')
router.register(r'reservas', ReservaListCreateView, basename='reservas')

# Define las rutas específicas de la app 'cine'
urlpatterns = [
    path('', include(router.urls)),
]