from django import forms
from museos.models import Comentario
from museos.models import Configuracion


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
        instancia = super(ComentarioForm, self).save(commit=False)

        instancia.museo = museo
        instancia.configuracion = configuracion

        instancia.save()

#class CambiarEstilo(forms.ModelForm):
    

#class CambiarNombrePaginaUsuario(forms.ModelForm):
    #class Meta:
        #model =  Configuracion

