# cinemas_backend/urls.py
from django.contrib import admin
from django.urls import path, include # ¡Asegúrate de que 'include' esté importado!

# Define las rutas principales del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea conecta todas las URLs de 'cine/urls.py' bajo el prefijo 'api/'
    path('api/', include('cine.urls')),
]