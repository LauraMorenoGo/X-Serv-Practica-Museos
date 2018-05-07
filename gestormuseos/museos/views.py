from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Museo, Configuracion, Comentario


class Barra(View):  #View es una clase de la que heredo

    def get(self, request):
        context = {}

        museos = Museo.objects.all()
        configuraciones = Configuracion.objects.all()

        context['museos'] = museos
        context['configuraciones'] = configuraciones

        return render(request, 'museos/main.html', context)



class Usuario(View):

    def get(self, request, id):

        context = {}

        usuarios = Configuracion.objects.exclude(id=id)

        try:
            usuario = Configuracion.objects.get(id=id)
        except ConfiguracionDoesNotExist:   #Cuando el id no es un número correcto
            usuario = None

        favoritos = usuario.favoritos.all()

        context['usuario'] = usuario
        context['usuarios'] = usuarios
        context['favoritos'] = favoritos

        return render(request, 'museos/usu.html', context)
    

class MuseoDetalle(View):

    def get(self, request, id):

        context = {}

        museo = Museo.objects.filter(id=id).first()

        context['museo'] = museo
        context['comentarios'] = museo.comentarios.all()

        
        return render(request, 'museos/mus.html', context)


    

