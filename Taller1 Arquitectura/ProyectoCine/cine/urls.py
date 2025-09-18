# cine/urls.py
from django.urls import path
from .views import PeliculaListCreateView, UsuarioListCreateView, ReservaListCreateView

# Define las rutas específicas de la app 'cine'
urlpatterns = [
    path('peliculas/', PeliculaListCreateView.as_view(), name='peliculas'),
    path('usuarios/', UsuarioListCreateView.as_view(), name='usuarios'),
    path('reservas/', ReservaListCreateView.as_view(), name='reservas'),
]