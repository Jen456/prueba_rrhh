from django.db import models

# Create your models here.

class InicioSesion(models.Model):
    users= models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    ruc = models.CharField(max_length=13)
    