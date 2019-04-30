from django.db import models   

# Create your models here.

class Tipo_de_Usuario(models.Model):

    nome = models.CharField(max_length=100)

    class Meta:

        verbose_name_plural = "Tipo de Usuário"

    def __str__(self):
        return self.nome 


class Usuario(models.Model):
   
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=9, primary_key=True)
    email = models.EmailField(max_length=100)
    tipo_de_usuario = models.ForeignKey(Tipo_de_Usuario, on_delete=models.PROTECT)

    class Meta:

        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.matricula    