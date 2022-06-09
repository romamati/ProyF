from django.db import models

class indumentarias(models.Model):
    codigo_barra = models.CharField(max_length=40, unique = True)
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    talle = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    cod_categoria = models.IntegerField()
    imagen = models.ImageField(upload_to="indumentaria",null=True)

    class Meta:
        verbose_name = 'indumentaria'
        verbose_name_plural = 'indumentarias'

    def __str__(self):
        return F'Producto {self.nombre} cuesta un total de ${self.precio}'

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

    def __str__(self):
        return F'Producto {self.nombre} cuesta un total de ${self.precio}'

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

    def __str__(self):
        return F'Producto {self.nombre} cuesta un total de ${self.precio}'