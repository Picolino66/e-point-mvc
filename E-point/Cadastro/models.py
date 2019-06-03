import re
from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf import settings

# Create your models here.

class Tipo_de_Usuario(models.Model):

    nome = models.CharField(max_length=100)

    class Meta:

        verbose_name = 'Tipo de Usuário'
        verbose_name_plural = 'Tipo de Usuário'

    def __str__(self):
        return self.nome 


class Usuario(models.Model):
   
    Id_de_Usuario = models.CharField(max_length=100, verbose_name='Id de Usuário', blank=True, default='')
    nome = models.CharField(max_length=50, verbose_name='Nome', unique=True)
    matricula = models.CharField(max_length=9, primary_key=True, verbose_name='Matrícula')
    email = models.EmailField(max_length=100, verbose_name='Email', unique=True)
    tipoUsuario = models.ForeignKey(Tipo_de_Usuario, on_delete=models.PROTECT, verbose_name='Tipo de Usuário')

    class Meta:

        verbose_name= 'Usuários'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.matricula 
