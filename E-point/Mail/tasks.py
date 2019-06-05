from __future__ import absolute_import
import time
from celery import shared_task
from celery.schedules import crontab

# from relatorios import gerar_relatorio_excel

@shared_task(queue='default') #1
def slow_task():
    print('Started task, processing...')
    time.sleep(120)
    print('Finished Task')
    return True
slow_task.delay(60) #2

