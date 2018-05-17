import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Museo, Configuracion, Comentario, Favorito
from django.contrib.auth.models import User
from museos.forms import ComentarioForm, CambiarEstiloForm, CambiarNombrePagForm
from django.http import HttpResponseRedirect
from museos.utils import CargarBaseDatos
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count

NUM_MUSEOS = 5

#PÁG PRINCIPAL
class Barra(View):  #View es una clase de la que heredo

    def get(self, request):
        context = {}


        check_acc = request.GET.get('acc')
        if not check_acc:
            museos = Museo.objects.all().annotate(num_comentarios=Count('comentarios')).order_by('-num_comentarios')[:NUM_MUSEOS]
            
        else:
            museos = Museo.objects.filter(accesibilidad=1).annotate(num_comentarios=Count('comentarios')).order_by('-num_comentarios')[:NUM_MUSEOS]
            
        configuraciones = Configuracion.objects.all()
    

        context['museos'] = museos
        context['configuraciones'] = configuraciones


        return render(request, 'museos/main.html', context)


#PÁG DE LOS MUSEOS DE UN USUARIO
class Usuario(View):

    def get(self, request, *args, **kwargs):    # *args: para tomar una cantidad indefinida de argumentos, devuelve lista
                                                # *kwargs: diccionario que contiene cada uno de los argumentos y su valor
        
        context = {}
        logged = ""
        id_user = kwargs.get('id')
        usuarios = Configuracion.objects.exclude(id=id_user)

        try:
            usuario = Configuracion.objects.get(id=id_user)
        except ObjectDoesNotExist:   #Cuando el id no es un número correcto
            usuario = None
        favoritos = Favorito.objects.all() 
        
        context['usuario'] = usuario
        context['usuarios'] = usuarios
        context['favoritos'] = favoritos
        form_nombre = CambiarNombrePagForm()
        context['form_nombre'] = form_nombre
        form_estilo = CambiarEstiloForm()
        context['form_estilo'] = form_estilo

        usuario_log = request.user.id
        context['usuario_ppal'] = str(usuario_log) == str(id_user)
        
        return render(request, 'museos/usu.html', context)

#POST PARA FORMULARIO QUE CAMBIA NOMBRE PÁG
class CambiaNombre(View):

    def post(self, request, **kwargs):
        
        configuracion = request.user.config

        form_nombre = CambiarNombrePagForm(request.POST, instance=configuracion)

        if form_nombre.is_valid():
            form_nombre.save()

        context = {
            'form_nombre': form_nombre,
            'configuracion': configuracion
        }
        return HttpResponseRedirect('/usuario/%s' % kwargs.get('id'))

#POST PARA FORMULARIO QUE CAMBIA ESTILO PÁG
class CambiaEstilo(View):

     def post(self, request, **kwargs):
        
        configuracion = request.user.config

        form_estilo = CambiarEstiloForm(request.POST, instance=configuracion)
        
        if form_estilo.is_valid():
            form_estilo.save()

        context = {
            'form_estilo': form_estilo,
            'configuracion': configuracion
        }
        return HttpResponseRedirect('/usuario/%s' % kwargs.get('id'))

#PÁGINA DE UN MUSEO EN CONCRETO
class MuseoDetalle(View):

    def get(self, request, **kwargs):

        context = {}
        user = request.user #sacamos la configuracion
        museo = Museo.objects.filter(id=kwargs.get('id')).first()   #Devuelve el valor con la clave 'id' y sino devuelve True
                                                                    #first() se queda con el primero y si no hay, nulo
        if not museo:   #necesito hacer un response redirect en django, me redirige a la pág ppal si no es válido
            return HttpResponseRedirect('/')

        context['is_fav'] = museo.favoritos.filter(configuracion=user.config).count()#<-- id ¿  id de config
        context['museo'] = museo
        context['comentarios'] = museo.comentarios.all()
        form = ComentarioForm()
        context['form'] = form

        
        return render(request, 'museos/mus.html', context)

    def post(self, request, **kwargs):
        
        configuracion = request.user.config
        museo = Museo.objects.filter(id=kwargs.get('id')).first()
        if not museo:   #necesito hacer un response redirect en django
            return HttpResponseRedirect('/')

        form = ComentarioForm(request.POST)

        if form.is_valid():
            form.save(museo, configuracion)
            return HttpResponseRedirect('/museos/%s' % kwargs.get('id'))

        context = {
            'museo': museo,
            'comentarios': museo.comentarios.all(),
            'form': form
        }
        return render(request, 'museos/mus.html', context)

#CARGO LA BASE DE DATOS
class LlamadaCargaBaseDatos(View):

    def get(self, request, *args, **kwargs):   
        
        cargar_datos = CargarBaseDatos()    #creamos la instancia a partir del objeto
        cargar_datos.ejecutar()
        
        return HttpResponseRedirect('/')

#AÑADIR A FAVORITOS
class Add(View):

    def get(self, request, *args, **kwargs):   
        
        user = request.user
        if user:

            museo = Museo.objects.filter(id=kwargs.get('id')).first()
            if museo:

                if not Favorito.objects.filter(museo=museo, configuracion=user.config):
                    Favorito(museo=museo, configuracion=user.config, fecha=datetime.datetime.today()).save()
                
        return HttpResponseRedirect('/museos/%s' % kwargs.get('id')) # vuelvo al detalle del museo
#QUITAR DE FAVORITOS
class Remove(View):

    def get(self, request, *args, **kwargs):   
        
        user = request.user
        if user:

            museo = Museo.objects.filter(id=kwargs.get('id')).first()
            if museo:

                favorito = Favorito.objects.filter(museo=museo, configuracion=user.config, fecha=datetime.datetime.today())
                favorito.delete()
        
        return HttpResponseRedirect('/museos/%s' % kwargs.get('id')) # vuelvo al detalle del museo

#PÁG CON EL LISTADO DE TODOS LOS MUSEOS
class Museos(View):

    def get(self, request):
        context = {}

        check_acc = request.GET.get('acc')
        if not check_acc:
            museos = Museo.objects.all()
        else:
            museos = Museo.objects.filter(accesibilidad=1)  #FILTRA LOS MUSEOS POR ACCESIBLES
        
        context['museos'] = museos

        return render(request, 'museos/lista_mus.html', context)

    def post(self, request, **kwargs):  #FILTRA LOS MUSEOS POR DISTRITO
        context = {}

        check_acc = request.GET.get('acc')
        if not check_acc:
            museos = Museo.objects.all()
        else:
            museos = Museo.objects.filter(accesibilidad=1)
        distrito_selected = request.POST.get('distrito')
        if distrito_selected:

            museos_final = museos.filter(distrito=distrito_selected.upper())

        context['museos'] = museos_final

        return render(request, 'museos/lista_mus.html', context)

#ABOUT
class About(View):

    def get(self, request):
        context = {}

        context['about'] = 'active'
        context['user'] = request.user

        return render(request, 'museos/about.html', context)

#USUARIO/XML
class UsuarioXml(View):

    def get(self, request, **kwargs):

        context = {}

        usuarios = Configuracion.objects.exclude(id=kwargs.get('id'))

        try:
            usuario = Configuracion.objects.get(id=kwargs.get('id'))
        except ConfiguracionDoesNotExist:   #Cuando el id no es un número correcto
            usuario = None

        favoritos = Favorito.objects.all() 

        context['favoritos'] = favoritos
        context['usuario'] = usuario

        return render(request, 'museos/usu_xml.html', context, content_type="text/xml")
        
class Accesibles(View):

    def get(self, request):
        context = {}

        museos = Museos.objects.filter(accesibilidad=1)

        context["museos"] = museos

        return render(request, 'museos/accesibles.html', context)