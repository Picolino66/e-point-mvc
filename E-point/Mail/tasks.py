from __future__ import absolute_import
from celery import shared_task
from relatorios import gerar_relatorio_excel

@shared_task
def gerar_relatorio2():

    return ""