from django import forms
from .models import Clase1, Clase2, Clase3

class FormularioDatos(forms.ModelForm):
    class Meta:
        model = Clase1 
        fields = '__all__'

class FormularioBusqueda(forms.Form):
    busqueda = forms.CharField(max_length=100)