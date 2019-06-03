from django.contrib import admin
from .models import Tipo_de_Usuario
from .models import Usuario

# Register your models here.

admin.site.register(Tipo_de_Usuario)
admin.site.register(Usuario)
