from django.shortcuts import render
from django.core.mail import send_mail
# from .models import Log_Usuario
import json
import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_POST

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
    # data['Log_Usuario'] = Log_Usuario.objects.all()

    return render(request, 'Mail/log.html', data)
 
@require_POST
@csrf_exempt
def new_log(request):
    print('entrou')
    print(request.POST)
    print(request.data)
    #Novo ponto de entrada
    # def new_entry(entry):

    #     return

    # def new_out(out):

    #     return    

    # activity = json.loads(request.body)
    # activity_time = datetime.date.strptime()
    # actvity = json.load(request.body)

    return HttpResponse(json.dumps(response), content_type="aplication/json")

    #return HttpResponse("aaaaaaaaa")
    #return HttpResponse('aaaa')
