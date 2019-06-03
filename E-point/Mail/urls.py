from django.urls import path, include
from .views import index

app_name = 'Mail'

urlpatterns = [
    path('', index),
]