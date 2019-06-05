import time
# from SistemaCadastro.tasks import add
from celery import shared_task
from django.shortcuts import render, redirect
from .models import Usuario
from .forms import Usuario_Form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def listagem(request):

    data = {}
    data['Usuários'] = Usuario.objects.all()

    return render(request, 'Cadastro/listagem.html', data)

def login(request):

    # form = request.POST
    # if form.is_valid():
    #     form.save()
    #     return redirect('admin')

    
    return render(request, 'Cadastro/login.html')

def cadastro(request):

    data = {}
    form = Usuario_Form(request.POST or None)
    
    if form.is_valid():
        form.save()    
        return redirect('listagem')

    data['form'] = form
    return render(request, 'Cadastro/cadastro.html', data)

def update(request, pk):

    data = {}
    usuario = Usuario.objects.get(pk=pk)
    form = Usuario_Form(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('listagem')
    
    data['form'] = form

    return render(request, 'Cadastro/cadastro.html', data)
    

# def login_validation(request):
#     message = "Login invalido !"
#     form = Login
#     if request.POST:
#         user = authenticate(request, user='admin', password=request.POST['senha'])
#         print(user)
#         if user is not None:
#             login(request, user)
#             message = "Parabens, você fez login!"
    
#     return render(request, 'Cadastro/login.html', context={"message": message})









