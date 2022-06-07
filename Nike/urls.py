from django.urls import path

from Nike.views import products, contacto, create_product_view, search_product_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('', products, name = 'products'),
    path('contacto/', contacto, name = 'contacto'),
    path('create-product/', create_product_view, name = 'create-product'),
    path('search-product/', search_product_view, name = 'search_product_view')
]

