from django import forms
from .models import Depoimento

class DepoimentoForm(forms.ModelForm):

    class Meta:
        model = Depoimento
        fields = ('empresa', 'avaliacao', 'recomendacao')