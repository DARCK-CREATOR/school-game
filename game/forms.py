from django import forms
from .models import Inscription

class Formulaire(forms.ModelForm):
 
    class Meta:
        model = Inscription
        fields = "__all__"
        widgets = {"password":forms.PasswordInput() }
       

