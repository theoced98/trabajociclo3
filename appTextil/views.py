import email
from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here. Modelos para el CRUD 

#Tabla empresas
class empresaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,NIT=""):
        if len(NIT)>0:
            emp=list(empresa.objects.filter(nit=NIT).values())
            if len(emp)>0:
                datos={"MensajeEM":emp,"mensaje":"Mostrando empresa..."}
            else:
                datos={"ErrorE":"Tal empresa no existe."}
        else: 
            empr=list(empresa.objects.values())
            if len(empr)>0:
                datos={"MensajeEM":empr,"mensaje":"Mostrando empresas..."}
            else:
                datos={"ErrorE":"No hay empresas."}
        return JsonResponse(datos)

    def post(self,request):
        datos2=json.loads(request.body)
        empres=empresa(nombre=datos2["Nombre"],direccion=datos2["Dirección"],telefono=datos2["Telef"],nit=datos2["NIT"])
        empres.save()
        respuesta={"MensajeEM":"La empresa ha sido guardada"}
        return JsonResponse(respuesta)

    def put(self,request,NIT):
        datos3=json.loads(request.body)
        empresact=list(empresa.objects.filter(nit=NIT).values())
        if len(empresact)>0:
            emp=empresa.objects.get(nit=NIT)
            emp.nombre=datos3["Nombre"]
            emp.direccion=datos3["Dirección"]
            emp.telefono=datos3["Telefono"]
            emp.save()
            mensaje={"Mensaje":"Datos de la Empresa actualizado"}
        else:
            mensaje={"Mensaje":"No existe la empresa que buscas."}
        return JsonResponse(mensaje)

    def delete(self,request,NIT=""):
        if len(NIT)>0:
            empdelete=list(empresa.objects.filter(nit=NIT).values())
            if len(empdelete)>0:
                empresa.objects.get(nit=NIT).delete()
                mensaje={"MensajeEM":"Datos de la empresa eliminados."}
            else:
                mensaje={"MensajeEM":"La empresa a eliminar no existe."}
        else:
            mensaje={"Advertencia":"Por favor ingresa el NIT"}
        return JsonResponse(mensaje)

class usuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,ID=0):
        if ID>0:
            user=list(usuario.objects.filter(user_id=ID).values())
            if len(user)>0:
                datos={"MensajeU":user,"mensaje":"Usuario Encontrado"}
            else:
                datos={"ErrorU":"Tal usuario no existe."}
        else: 
            usuar=list(usuario.objects.values())
            if len(usuar)>0:
                datos={"MensajeU":usuar}
            else:
                datos={"ErrorU":"No hay usuarios registrados."}
        return JsonResponse(datos)

    def post(self,request):
        datosuser=json.loads(request.body)
        guardarusuario=usuario(nombre=datosuser["Nombre"],email=datosuser["Correo"],
        password=datosuser["Contrase"],telefono=datosuser["Telefono"],tipouser=datosuser["Tipo"])
        guardarusuario.save()
        respuesta={"MensajeU":"El usuario ha sido guardado"}
        return JsonResponse(respuesta)

    def put(self,request,ID):
        datos3=json.loads(request.body)
        userupdate=list(usuario.objects.filter(user_id=ID).values())
        if len(userupdate)>0:
            usua=usuario.objects.get(user_id=ID)
            usua.nombre=datos3["Nombre"]
            usua.email=datos3["Correo"]
            usua.telefono=datos3["Telefono"]
            usua.tipouser=datos3["Tipo"]
            usua.save()
            mensaje={"MensajeU":"Datos del usuario actualizado"}
        else:
            mensaje={"MensajeU":"No existe el usuario que buscas."}
        return JsonResponse(mensaje)

    def delete(self,request,ID):
        eliminaruser=list(usuario.objects.filter(user_id=ID).values())
        if len(eliminaruser)>0:
            usuario.objects.get(user_id=ID).delete()
            mensaje={"MensajeU":"Datos del usuario eliminados."}
        else:
            mensaje={"MensajeU":"El usuario a eliminar no existe."}
        return JsonResponse(mensaje)

class registro_contableView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,ID=0):
        if ID>0:
            regis=list(registro_contable.objects.filter(idregis=ID).values())
            if len(regis)>0:
                datos={"mensajeR":regis,"mensaje":"Mostrando Registro existente"}
            else:
                datos={"ErrorC":"Tal registro no existe."}
        else: 
            regist=list(registro_contable.objects.values())
            if len(regist)>0:
                datos={"mensajeR":regist,"mensaje":"Mostrando Registros Existentes..."}
            else:
                datos={"ErrorC":"No hay Registros Existentes"}
        return JsonResponse(datos)

    def post(self,request):
        datosregi=json.loads(request.body)
        try:
            empre=empresa.objects.get(nit=datosregi["NIT"])
            usua=usuario.objects.get(user_id=datosregi["ID"])
            guardarregistro=registro_contable.objects.create(empresa_id=empre,idusuario=usua,tipo=datosregi["Tipo"],valor=datosregi["Valor"])
            guardarregistro.save()
            respuesta={"mensajeR":"El registro ha sido guardado"}
        except usuario.DoesNotExist:
            respuesta={"Advertencia":"Usuario Inexistente"}
        except empresa.DoesNotExist:
            respuesta={"Advertencia":"Empresa inexistente"}

        return JsonResponse(respuesta)
    
    def delete(self,request,ID):
        eliminarregistro=list(registro_contable.objects.filter(idregis=ID).values())
        if len(eliminarregistro)>0:
            registro_contable.objects.get(idregis=ID).delete()
            mensaje={"mensajeR":"Registro Eliminado"}
        else:
            mensaje={"mensajeR":"El registro a eliminar no existe"}
        return JsonResponse(mensaje)

class empleadoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,ID=0):
        if ID>0:
            employer=list(empleado.objects.filter(empleado_id=ID).values())
            if len(employer)>0:
                datos={"MensajeEMP":"Empleado Existente"}
            else:
                datos={"ErrorEMP":"Tal empleado no existe."}
        else: 
            empl=list(empleado.objects.values())
            if len(empl)>0:
                datos={"MensajeEMP":empl}
            else:
                datos={"ErrorEMP":"No hay empleados Existentes"}
        return JsonResponse(datos)

    def post(self,request):
        datosempleado=json.loads(request.body)
        try:
            empre=empresa.objects.get(nit=datosempleado["NIT"])
            user=usuario.objects.get(user_id=datosempleado["ID Usuario"])
            guardarempleado=empleado.objects.create(empresa_id=empre,usuarid=user)
            guardarempleado.save()
            respuesta={"MensajeEMP":"El empleado ha sido guardado"}
        except usuario.DoesNotExist:
            respuesta={"Advertencia":"Usuario Inexistente"}
        except empresa.DoesNotExist:
            respuesta={"Advertencia":"Empresa inexistente"}

        return JsonResponse(respuesta)

    def delete(self,request,ID):
        eliminarempleado=list(empleado.objects.filter(empleado_id=ID).values())
        if len(eliminarempleado)>0:
            empleado.objects.get(empleado_id=ID).delete()
            mensaje={"MensajeEMP":"Datos del empleado eliminados."}
        else:
            mensaje={"Mensaje":"El empleado a eliminar no existe."}
        return JsonResponse(mensaje)