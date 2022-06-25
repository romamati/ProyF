from django.contrib import admin

#from products.models import Products, Categoria
from Nike.models import indumentarias,calzados,accesorios,Avatar

# Register your models here.
admin.site.register(indumentarias)
admin.site.register(calzados)
admin.site.register(accesorios)
admin.site.register(Avatar)