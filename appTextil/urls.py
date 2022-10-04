from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
from .viewLogin import *
from .viewsFront import *

urlpatterns=[
    path('Empresas/',empresaView.as_view(),name="Listado de Empresas"),
    path('Empresas/<str:NIT>',empresaView.as_view(),name="Busqueda de Empresas"),
    path('Usuarios/',usuarioView.as_view(),name='Usuarios'),
    path('Usuarios/<int:ID>',usuarioView.as_view(),name='BuscarUser'),
    path('Registro/',registro_contableView.as_view(),name="ListadoRegistro"),
    path('Registro/<int:ID>',registro_contableView.as_view(),name="BusquedaRegistro"),
    path('Empleados/',empleadoView.as_view(),name="ListadoEmpleados"),
    path('Empleados/<int:ID>',empleadoView.as_view(),name='BusquedaEmpleados'),
    path('',inicio, name="Inicio"),
    path('Sesion/',iniciarSesion, name="Ingreso"),
    path('CerrarSesion/',cerrarSesion,name="Cerrar"),
    path('Registros/',listaRegistros,name="Registros"),
    path('consultaRegistro/',consultaRegistro,name='ConsultaRegistros'),
    path('formRegistro/',formularioRegistro,name="FormRegistro"),
    path('guardarRegistro/',guardarRegistro,name="GuardarRegistro"),
    path('Usuario/',listaUsuarios, name="ListaUsuario"),
    path('consultaUsuario/',consultaUsuario,name="ConsultaUsuario")
]