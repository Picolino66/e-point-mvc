from django.shortcuts import render, redirect
from .models import Usuario
from .forms import Usuario_Form

# Create your views here.

def listagem(request):

    data = {}
    data['Usuários'] = Usuario.objects.all()

    return render(request, 'Cadastro/listagem.html', data)

def login(request):

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


