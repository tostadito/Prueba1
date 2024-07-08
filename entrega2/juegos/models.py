from django.db import models

# Create your models here.

class Juego(models.Model):
    idJuego = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.CharField(max_length=100)

class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
