from django.db import models

# Create your models here.

class carro (models.Model):
    Id = models.AutoField(primary_key=True),
    modelo = models.CharField(max_length=25),
    marca = models.CharField(max_length=25),
    color = models.CharField(max_length=25)

class Coche(models.Model):
    ID = models.AutoField(primary_key=True),
    marca = models.CharField(max_length=25),
    color = models.CharField(max_length=25),
    modelo = models.CharField(max_length=25)
