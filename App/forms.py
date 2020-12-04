from django import forms
from .models import Nombre


class NombreForm(forms.ModelForm):
    class Meta:
        model = Nombre
        fields = ['nombre', 'codigo', 'grupo']
