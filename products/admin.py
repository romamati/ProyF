from django.contrib import admin

#from products.models import Products, Categoria
from products.models import indumentarias,calzados,accesorios

# Register your models here.
admin.site.register(indumentarias)
admin.site.register(calzados)
admin.site.register(accesorios)