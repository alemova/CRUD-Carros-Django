"""
URL configuration for django_crud_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from carro import views

app_name = "carro"
urlpatterns = [
    path('admin/', admin.site.urls),               #URL Default de admin
    path('carros', views.Carros, name="home"),        #vista principal para observar listado de carros
    path('carros/crear', views.formCar),              #renderiza la vista del formulario para crear carro
    path('carro/<Id>', views.CarroId),                 #renderiza la vista para editar/seleccionar un carro
    path('ActualizarCarro<Id>', views.ActualizarCarro),   #URL para actualizar un registro
    path('carroNuevo', views.CrearCarro),             #URL para crear un registro
    path('borrarCarro/<Id>', views.BorrarCarro)   #URL para eliminar un registro

]
