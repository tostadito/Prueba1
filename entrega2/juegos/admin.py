from django.contrib import admin
from .models import Juego
from .models import Usuario

# Register your models here.

admin.site.register(Juego)
admin.site.register(Usuario)