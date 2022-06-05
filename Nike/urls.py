from django.contrib import admin
from django.urls import path
from Nike.views import producto_add

urlpatterns = [
    path('',producto_add,name='producto_add'),
]
