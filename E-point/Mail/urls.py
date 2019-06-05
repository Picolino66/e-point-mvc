from django.urls import path, include
from .views import index
from .views import new_log

app_name = 'Mail'

urlpatterns = [
    path('', index),
]