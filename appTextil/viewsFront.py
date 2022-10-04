from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests #:0
import json

def inicio(request):
    return render(request,"index.html")

def listaRegistros(request):
    response=requests.get("http://127.0.0.1:8000/Inicio/Registro/")
    registro=response.json()
    print(registro)
    return render(request,"Empleado.html",registro)

def consultaRegistro(request):
    dato=request.POST['idregis'] #Aca va el nombre del input del formulario del html
    response=requests.get("http://127.0.0.1:8000/Inicio/Registro/"+dato)
    registro1=response.json()
    print(registro1)
    return render(request,"Empleado.html",registro1)

def formularioRegistro(request):
    return render(request,"formRegistro.html")

def guardarRegistro(request):
    datosr={
        "NIT":request.POST['empresa_id'],
        "ID":request.POST['userid'],
        "Tipo":request.POST['tipo'],
        "Valor":request.POST['valor']
    }
    requests.post("http://127.0.0.1:8000/Inicio/Registro/",data=json.dumps(datosr))
    return redirect ('../Registros/')

def listaUsuarios(request):
    response=requests.get("http://127.0.0.1:8000/Inicio/Usuarios/")
    usuario1=response.json()
    print(usuario1)
    return render(request,"Visitante.html",usuario1)

def consultaUsuario(request):
    dato=request.POST['iduser'] #Aca va el nombre del input del formulario del html
    response=requests.get("http://127.0.0.1:8000/Inicio/Usuarios/"+dato)
    usuario1=response.json()
    print(usuario1)
    return render(request,"Visitante.html",usuario1)

def cargarForm(request,ID):
    response=requests.get('http://127.0.0.1:8000/Inicio/Usuarios/'+ID)
    usera=response.json()
    print(usera)
    return render(request,'formActualizar.html', usera)