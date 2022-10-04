from enum import unique
from django.db import models
from email.policy import default
from random import choices
from django.db import models
from .choices import tipos, usuariostipo

# Create your models here.

class empresa(models.Model):
    empresa_id=models.AutoField(auto_created=True,primary_key=True)
    nombre=models.CharField(max_length=50, null=False)
    direccion=models.CharField(max_length=50, null=False)
    telefono=models.CharField(max_length=50, null=False)
    nit=models.CharField(unique=True, max_length=25)

    def __str__(self) -> str:
        return self.nombre

class usuario(models.Model):
    user_id = models.AutoField(auto_created=True, primary_key= True)
    nombre = models.CharField(max_length= 25)
    email = models.EmailField(unique= True)
    password = models.CharField(max_length= 50)
    telefono = models.CharField(max_length= 50)
    tipouser=models.CharField(max_length=1,choices=usuariostipo,default='V')

class registro_contable(models.Model):
    idregis=models.AutoField(auto_created=True,primary_key=True)
    fecha=models.DateField(auto_now=True)
    empresa_id= models.ForeignKey(empresa, on_delete=models.CASCADE)
    idusuario=models.ForeignKey(usuario, on_delete=models.CASCADE,null=True)
    tipo=models.CharField(max_length=1,choices=tipos,default='I')
    valor=models.IntegerField(null=True)

class empleado(models.Model):
    empleado_id= models.AutoField(auto_created=True,primary_key=True)
    empresa_id= models.ForeignKey(empresa,on_delete=models.CASCADE)
    usuarid= models.ForeignKey(usuario, on_delete=models.CASCADE)

