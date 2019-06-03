from django.db import models

# Create your models here.

class Log_Usuario(models.Model):

    Id_Card = models.CharField(max_length=100, verbose_name='Id da Carteirinha')
    horarioEntrada = models.DateTimeField(verbose_name='Horário de Entrada', auto_now_add=True)
    horarioSaida = models.DateTimeField(verbose_name='Horário de Saída', auto_now_add=True)
    Status = models.IntegerField(verbose_name='Status')
    
    class Meta:

        verbose_name_plural = "Log de Usuários"
        verbose_name = "Log de Usuário"

    def __str__(self):
        return self.Id_Card 
