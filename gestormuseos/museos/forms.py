from django import forms
from museos.models import Comentario, Configuracion, Museo


#FORMULARIO PARA AÑADIR COMENTARIOS
class ComentarioForm(forms.ModelForm):  #Sacado de stackoverflow
    class Meta:
        model = Comentario
        fields = ['comentario']

    def clean_comentario(self): #Validación

        comentario = self.cleaned_data.get('comentario')

        if 'kk' in comentario:
            raise forms.ValidationError("No está permitido poner eso")

        return comentario


    def save(self, museo, configuracion, commit=False):
        instancia = super(ComentarioForm, self).save(commit=False) #Llama al padre

        instancia.museo = museo
        instancia.configuracion = configuracion

        instancia.save()

#FORMULARIO PARA CAMBIAR EL ESTILO CSS DE LA PÁG DE USUARIO
class CambiarEstiloForm(forms.ModelForm):
    class Meta:
        model = Configuracion
        fields = ['fondo', 'letra']

#FORMULARIO PARA CAMBIAR EL NOMBRE DE LA PÁG DE USUARIO
class CambiarNombrePagForm(forms.ModelForm):
    class Meta:
        model = Configuracion
        fields = ['nombre_pag']

#FORMULARIO PARA FILTRAR LOS MUSEOS POR DISTRITO
class DistritoForm(forms.ModelForm):
    class Meta:
        model = Museo
        fields = ['distrito']

    def filtrar(self, distrito):
        museo = Museo.objects.filter(distrito='distrito')

