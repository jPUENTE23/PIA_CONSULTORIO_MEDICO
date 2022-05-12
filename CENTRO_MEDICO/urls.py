"""CENTRO_MEDICO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from Citas.views import vistaRegistro, main, agregarRegistro
from Citas.views import verificarConsultas, listadoDoctores, agregarDoctor
from Pagos.views import pagos, consultarPagos, eliminarPago


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main, name='main'),
    path('RegistroCitas/', vistaRegistro, name='RegistroCitas'),
    path('verificarConsultas/', verificarConsultas, name='verificarConsultas'),
    path('verificarConsultas/genPago/<int:idCita>', pagos, name='pagos'),
    path('consultarPagos/', consultarPagos, name='consultarPagos'),
    path('verificarConsultas/<int:NoCita>', pagos, name='Pagos'),
    path('RegistroCitas/agregarRegistro/', agregarRegistro, name='agregarRegistro'),
    path('listadoDoctores/', listadoDoctores, name='listadoDoctores'),
    path('listadoDoctores/agregarDoctor/', agregarDoctor, name='agregarDoctor'),
    path('consultarPagos/eliminarPago/<int:idPago>', eliminarPago, name='eliminarPago')

]
