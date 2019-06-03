"""SistemaCadastro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Cadastro.views import listagem, login, cadastro, update 
# login_validation
from Mail.views import log
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('cadastro/', cadastro, name='novo_cadastro'),
    path('listagem/', listagem, name='listagem'),
    path('update/<int:pk>/', update, name='update'),
    # path('login/', login_validation, name='login-success'),
    # path('', login),
    # Login & logout URLs
    path('', LoginView.as_view() , name='login'),
    path('sendmail/', include('Mail.urls')),
    path('log_view/', log, name='log'),
]
