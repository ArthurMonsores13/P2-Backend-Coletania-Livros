from django import forms
from .models import Filme


class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ["titulo", "diretor", "ano", "genero", "nota"]
        widgets = {
            "nota": forms.NumberInput(attrs={"min": 1, "max": 10}),
        }