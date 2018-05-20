from django.contrib import admin
from museos.models import Museo, Configuracion, Comentario, Favorito

# Register your models here.

admin.site.register(Museo)
admin.site.register(Favorito)
admin.site.register(Configuracion)
admin.site.register(Comentario)
