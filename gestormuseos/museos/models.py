from django.db import models
from django.contrib.auth.models import User

#Nuestro modelo va a tener tres clases: Museo, Configuración, Comentario


class Museo(models.Model):
    id_externo = models.CharField(max_length=150) #No me deja ponerlo sin null
    nombre = models.CharField(max_length=150)
    descripcion_entidad = models.TextField(null=True)   #Ya que hay museos con este campo vacío
    horario = models.TextField(null=True, blank=True)
    equipamiento = models.TextField(null=True, blank=True)
    transporte = models.CharField(max_length=150, null=True, blank=True)    #Blank es para admitir texto vacío solo en CharField
    descripcion = models.TextField(null=True, blank=True)
    accesibilidad = models.IntegerField(null=True)
    content_url =  models.CharField(max_length=150, null=True, blank=True)
    nombre_via = models.CharField(max_length=150, null=True, blank=True)
    clase_via = models.CharField(max_length=150, null=True, blank=True)
    numero_via = models.CharField(max_length=150, null=True, blank=True)
    localidad = models.CharField(max_length=150, null=True, blank=True)
    provincia = models.CharField(max_length=150, null=True, blank=True)
    codigo_postal = models.CharField(max_length=150)
    barrio = models.CharField(max_length=150, null=True, blank=True )
    distrito = models.CharField(max_length=150, null=True, blank=True)
    coordenada_x = models.IntegerField(null=True)
    coordenada_y = models.IntegerField(null=True)
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)
    telefono = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    tipo = models.CharField(max_length=150, null=True, blank=True) #Todavía no sé para que me puede servir este campo

    def __str__(self):
        return self.nombre

class Favorito(models.Model):
    museo = models.ForeignKey(Museo, related_name='favoritos', null=False, blank=False)
    configuracion = models.ForeignKey('Configuracion', related_name='favoritos', null=False, blank=False)
    fecha = models.DateField()
    def __str__(self):
        return "%s %s %s" % (self.museo, self.configuracion.usuario, self.fecha )

    # def save(): # Hacer que cada ver que se modifique, se guarde la fecha actual. datetime.today()

class Configuracion(models.Model):
    usuario = models.OneToOneField(User, related_name='config', null=False)
    nombre_pag = models.CharField(max_length=150, null=True, blank=True)
    letra = models.IntegerField(null=True)
    fondo = models.CharField(max_length=150, null=True, blank=True)
    def __str__(self):
        return str(self.usuario)



class Comentario(models.Model):
    museo = models.ForeignKey(Museo, related_name='comentarios', null=False, blank=False)   #Un museo puede tener varios comentarios, pero un comentario sólo puede estar en un museo (Museo 1 - N Comentarios)
    configuracion =	models.ForeignKey(Configuracion, related_name='comentarios', null=False)    #Un usuario puede tener varios comentarios, pero un comentario es sólo de un usuario (Usuario 1 - N Comentarios)
    comentario = models.TextField()

    def __str__(self):
        return str(self.museo)
#Corregido error que me daba con stackoverflow "differentiate null=True, blank=True in django"
