from django.shortcuts import render
from django.core.mail import send_mail
from .models import Log_Usuario

# Create your views here.

def index(request):

    subject = 'Emakers Jr.'
    message = 'Você recebeu PCD!'
    email_from = 'settings.EMAIL_HOST_USER'
    recipient_list = ['otavioaugusto08@hotmail.com','otavioresende1998@gmail.com',]

    send_mail(subject, message, email_from, recipient_list, fail_silently=False)

    return render(request, 'Cadastro/index.html')

def log(request):
    
    data = {}
    data['Log_Usuario'] = Log_Usuario.objects.all()

    return render(request, 'Mail/log.html', data)