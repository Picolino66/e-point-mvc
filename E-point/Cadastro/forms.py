from django.forms import ModelForm
from django import forms
from .models import Usuario

class Usuario_Form(ModelForm):
    
    class Meta:
        
        model = Usuario
        fields = ['nome', 'matricula', 'email', 'tipoUsuario']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'matricula': forms.TextInput(attrs={'placeholder': 'Matŕicula'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }