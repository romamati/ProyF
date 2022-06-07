from django.db import models

#class Products(models.Model):
#    name = models.CharField(max_length=40)
#    price = models.FloatField()
#    description = models.CharField(max_length=200, blank=True, null=True)
#    SKU = models.CharField(max_length=30, unique=True)
#    active = models.BooleanField(default=True)

#    class Meta:
#        verbose_name = 'producto'
#        verbose_name_plural = 'productos'


#class Categoria(models.Model):
#    name = models.CharField(max_length=50)
#    description = models.CharField(max_length=100)

#    class Meta:
#        verbose_name = 'categoria'
#        verbose_name_plural = 'categorias'


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
    cod_categoria = models.IntegerField()
    imagen = models.ImageField(upload_to="indumentaria",null=True)

    class Meta:
        verbose_name = 'indumentaria'
        verbose_name_plural = 'indumentarias'

class calzados(models.Model):
    codigo_barra = models.CharField(max_length=40, unique = True)
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    talle = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    cod_categoria = models.IntegerField()
    imagen = models.ImageField(upload_to="calzado",null=True)

    class Meta:
        verbose_name = 'calzado'
        verbose_name_plural = 'calzados'

class accesorios(models.Model):
    codigo_barra = models.CharField(max_length=40, unique = True)
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    color = models.CharField(max_length=40)
    cod_categoria = models.IntegerField()
    imagen = models.ImageField(upload_to="accesorio",null=True)

    class Meta:
        verbose_name = 'accesorio'
        verbose_name_plural = 'accesorios'