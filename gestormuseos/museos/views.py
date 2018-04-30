from django.shortcuts import render
from django.http import HttpResponse
from .models import Museo, Configuracion, Comentario

def barra(request):
    respuesta = "<html>Museos registrados:<br></html>"
    lista = Museo.objects.all()
    for pag in lista:
        respuesta += "<br><li><a href='/museos/id'>" + pag.nombre + "</li></a>"
    respuesta += "<html><br>Museos favoritos de gente registrada:<br></html>"
    lista = Configuracion.objects.all()
    for pag in lista:
        respuesta += "<br><li><a href='/usuario'>" + str(pag.usuario) + "</li></a>"

    return HttpResponse(respuesta)


def usuario(request):
    lista = Configuracion.objects.all()
    for pag in lista:
        usuario = pag.usuario
        respuesta = "Los museosfavoritos de " + str(usuario) + " son:<br>"
        respuesta += str(pag.favoritos) + "<br>"
        respuesta += "<a href='/'>Volver a la página principal</a><br><a href='/admin'>Ir a la página de configuración</a>"

    return HttpResponse(respuesta)

def museo(request):
    lista = Comentario.objects.all()
    for pag in lista:
        respuesta ="Los comentarios del museo: " + pag.museo + "son los siguientes:<br>"
        respuesta += pag.comentario + "<br>"
        respuesta += "<a href='/'>Volver a la página principal</a><br><a href='/admin'>Ir a la página de configuración</a>"