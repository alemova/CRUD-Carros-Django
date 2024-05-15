from django.db import models

# Create your models here.

class carro (models.Model):
    Id = models.AutoField(primary_key=True, serialize=True, default=None)
    modelo = models.CharField(max_length=25, null=True)
    marca = models.CharField(max_length=25, null=True)
    color = models.CharField(max_length=25, null=True)

class Coche(models.Model):
    ID = models.AutoField(primary_key=True, serialize=True, default=None)
    marca = models.CharField(max_length=25, null=True)
    color = models.CharField(max_length=25, null=True)
    modelo = models.CharField(max_length=25, null=True)
