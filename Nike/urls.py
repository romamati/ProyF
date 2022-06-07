from django.urls import path

from Nike.views import products, create_product_view, search_product_view,crear_productos_calzados,buscar_productos_calzados,crear_productos_accesorios,buscar_productos_accesorios

from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('', products, name = 'products'),
    path('create-product/', create_product_view, name = 'create-product'),
    path('search-product/', search_product_view, name = 'search_product_view'),
    path('crear-productos-calzados/', crear_productos_calzados, name = 'crear-productos-calzados'),
    path('buscar-productos-calzados/', buscar_productos_calzados, name = 'buscar-productos-calzados'),
    path('crear-productos-accesorios/', crear_productos_accesorios, name = 'crear-productos-accesorios'),
    path('buscar-productos-accesorios/', buscar_productos_accesorios, name = 'buscar-productos-accesorios'),
]

