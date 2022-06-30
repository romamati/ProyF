from django.contrib import admin

#from products.models import Products, Categoria
from Nike.models import indumentarias,calzados,accesorios,Avatar,Categoria_Accesorio,Categoria_Calzado,Categoria_Indumentaria

# Register your models here.
admin.site.register(indumentarias)
admin.site.register(calzados)
admin.site.register(accesorios)
admin.site.register(Avatar)
admin.site.register(Categoria_Indumentaria)
admin.site.register(Categoria_Accesorio)
admin.site.register(Categoria_Calzado)