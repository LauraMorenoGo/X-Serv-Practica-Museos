from django.shortcuts import render
from django.http import HttpResponse
from .models import Museo, Configuracion, Comentario

def barra(request):
    respuesta = "<html>Museos registrados:<br></html>"
    lista = Museo.objects.all()
    for pag in lista:
        respuesta += "<br><li>" + pag.nombre + "</li>"
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
        respuesta += str(pag.favoritos)

    return HttpResponse(respuesta)