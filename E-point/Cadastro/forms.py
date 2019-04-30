from django.forms import ModelForm
from .models import Usuario

class Usuario_Form(ModelForm):
    
    class Meta:
        
        model = Usuario
        fields = ['nome', 'matricula', 'email', 'tipo_de_usuario']