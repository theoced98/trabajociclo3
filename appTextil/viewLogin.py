from wsgiref.util import request_uri
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .models import usuario
from django.contrib import messages

def iniciarSesion(request):

    if request.method == "POST":
        formulario=AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            useriname=formulario.cleaned_data.get("username")
            contrasena=formulario.cleaned_data.get("password")
            useri=authenticate(username=useriname, password=contrasena)
            if useri is not None: #Si este usuario no es nulo y este existe
                try:
                    usemp=usuario.objects.get(email=useri.email)
                    usemp=usuario.objects.filter(tipouser='E').values()
                    login(request, useri) #Inicia sesión
                    return render(request, "Empleado.html")
                except usuario.DoesNotExist:
                    if useri.is_superuser:
                        login(request, useri)
                        return redirect('Administrador.html')
                    else: 
                        messages.success(request,f'Acceso Resitringido')
                        return render(request,"Visitante.html")
            else: 
                messages.success(request,f'Usuario no existe')
        else:
            messages.success(request,f'Datos Erróneos')

    formulario=AuthenticationForm()
    return render(request,'login2.html')

def cerrarSesion(request):
    logout(request)
    return redirect("../Sesion/")