from django.db import models
from django.contrib.auth.models import User

#Nuestro modelo va a tener tres clases: Museo, Configuración, Comentario


class Museo(models.Model):
	nombre = models.CharField(max_length=150)
	descripcion_entidad = models.TextField(null=True)	#Ya que hay museos con este campo vacío
	horario = models.CharField(max_length=150, null=True, blank=True)	#Blank es para admitir texto vacío solo en CharField
	equipamiento = models.TextField(null=True)
	transporte = models.CharField(max_length=150)
	descripcion = models.TextField(null=True)
	accesibilidad = models.IntegerField()
	content_url =  models.CharField(max_length=150)
	nombre_via = models.CharField(max_length=150)
	clase_via = models.CharField(max_length=150)
	numero_via = models.CharField(max_length=150, null=True, blank=True)
	localidad = models.CharField(max_length=150)
	provincia = models.CharField(max_length=150)
	codigo_postal = models.CharField(max_length=150)
	barrio = models.CharField(max_length=150)
	distrito = models.CharField(max_length=150)
	coordenada_x = models.IntegerField()
	coordenada_y = models.IntegerField()
	latitud = models.FloatField()
	longitud = models.FloatField()
	telefono = models.CharField(max_length=150, null=True, blank=True)
	email = models.CharField(max_length=150, null=True, blank=True)
	tipo = models.CharField(max_length=150)		#Todavía no sé para que me puede servir este campo


class Configuracion(models.Model):
	favoritos = models.ManyToManyField(Museo, related_name='configuraciones', null=True)
	usuario = models.OneToOneField(User, related_name='config', null=False)
	



class Comentario(models.Model):
	museo = models.ForeignKey(Museo, related_name='comentarios', null=False)	#Un museo puede tener varios comentarios, pero un comentario sólo puede estar en un museo (Museo 1 - N Comentarios)
	configuracion =	models.ForeignKey(Configuracion, related_name='comentarios', null=False) #Un usuario puede tener varios comentarios, pero un comentario es sólo de un usuario (Usuario 1 - N Comentarios)
	comentario = models.TextField()