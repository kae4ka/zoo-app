from django import forms
from .models import Cages

class CagesForm(forms.ModelForm):
    class Meta:
        model= Cages
        fields= ["cage_name", "cage_type"]