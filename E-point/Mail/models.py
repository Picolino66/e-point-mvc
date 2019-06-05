from django.db import models
import datetime

#Create your models here.

class Log_Usuario(models.Model):

    Id_Card = models.CharField(max_length=100)
    Status = models.IntegerField()
    Entrou = models.BooleanField(default=False)
    Data_ano = models.IntegerField()
    Data_mes = models.IntegerField()
    Data_dia = models.IntegerField()
    Data_hora = models.IntegerField()
    Data_minuto = models.IntegerField()
    Data_segundo = models.IntegerField()

    class Meta:
        
        verbose_name_plural = "Log de Usuários"
        verbose_name = "Log de Usuário"

    def __str__(self):
        return self.Id_Card
