from django.db import models

# Create your models here.

#cod_estacion = 1 -> Verano
#cod_estacion = 2 -> Invierno
#cod_estacion = 3 -> Otoño

class indumentarias(models.Model):
    codigo_barra = models.CharField(max_length=40, unique = True)
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    talle = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    cod_estacion = models.IntegerField()

class calzados(models.Model):
    codigo_barra = models.CharField(max_length=40, unique = True)
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    talle = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    cod_categoria = models.IntegerField()

class accesorios(models.Model):
    codigo_barra = models.CharField(max_length=40, unique = True)
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    color = models.CharField(max_length=40)
    cod_categoria = models.IntegerField()

