from django.shortcuts import render
from django.http import HttpResponse
from .models import Museo, Configuracion, Comentario

def barra(request):

    context = {}

    museos = Museo.objects.all()
    configuraciones = Configuracion.objects.all()

    context['museos'] = museos
    context['configuraciones'] = configuraciones

    return render(request, 'museos/main.html', context)


def usuario(request, id):

    context = {}

    usuarios = Configuracion.objects.filter(id=id).first()

    context['usuarios'] = usuarios

    return render(request, 'museos/usu.html', context)



#    lista = Configuracion.objects.all()
#    for pag in lista:
#        usuario = pag.usuario
#        respuesta = "Los museos favoritos de " + str(usuario) + " son:<br>"

#        respuesta += str(pag.favoritos) + "<br>"
#        respuesta += "<a href='/'>Volver a la página principal</a><br><a href='/admin'>Ir a la página de configuración</a>"

#    return HttpResponse(respuesta)


def museo_detalle(request, id):

    context = {}

    museos = Museo.objects.filter(id=id).first()
    comentarios = Comentario.objects.filter(museo__id=id)   #Lo que hace es filtrar por el id del museo y obtener los comentarios de ese museo

    context['museos'] = museos
    context['comentarios'] = comentarios

    #try, except
    #try:
        #museo2 = Museo.objects.get(id=id)
    #except:    
        #raise    #levanta una excepción  

    #Otra opción
    #raise Exception(museo)
    
    return render(request, 'museos/mus.html', context)

    #for pag in lista:
    #    respuesta ="Los comentarios del museo: " + pag.museo + "son los siguientes:<br>"
    #    respuesta += pag.comentario + "<br>"
    #    respuesta += "<a href='/'>Volver a la página principal</a><br><a href='/admin'>Ir a la página de configuración</a>"

    #    respuesta += str(pag.favoritos)

    #return HttpResponse(respuesta)

#def todos_museos(request):

