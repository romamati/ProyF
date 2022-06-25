from django.urls import path

from Nike.views import buscar_productos_indumentarias,Pelota,Pulseras,Cantiplora,Anteojos,Muñequeras,Bolsos_Mochilas,Llaveros,Remeras,Camperas,Pantalones,Buzos,crear_productos_indumentarias,crear_productos_calzados,crear_productos_accesorios,calzado_view,indumentaria_view,accesorio_view,ZapatillaDeportiva,ZapatillaComunes,Botines,Ojotas

from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('ADDCalzados/', crear_productos_calzados, name = 'ADDCalzados'),
    path('ADDIndumentarias/', crear_productos_indumentarias, name = 'ADDIndumentarias'),
    path('ADDAccesorios/', crear_productos_accesorios, name = 'ADDAccesorios'),

    path('Indumentarias/', indumentaria_view, name = 'Indumentarias'),
    path('Calzados/', calzado_view, name = 'Calzados'),
    path('Accesorios/', accesorio_view, name = 'Accesorios'),

    path('Remeras/', Remeras, name = 'Remeras'),
    path('Camperas/', Camperas, name = 'Camperas'),
    path('Pantalones/', Pantalones, name = 'Pantalones'),
    path('Buzos/', Buzos, name = 'Buzos'),

    path('ZapatillaDeportiva/', ZapatillaDeportiva, name = 'ZapatillaDeportiva'),
    path('ZapatillaComunes/', ZapatillaComunes, name = 'ZapatillaComunes'),
    path('Botines/', Botines, name = 'Botines'),
    path('Ojotas/', Ojotas, name = 'Ojotas'),

    path('Pelota/', Pelota, name = 'Pelota'),
    path('Pulseras/', Pulseras, name = 'Pulseras'),
    path('Cantiplora/', Cantiplora, name = 'Cantiplora'),
    path('Anteojos/', Anteojos, name = 'Anteojos'),
    path('Muñequeras/', Muñequeras, name = 'Muñequeras'),
    path('Bolsos_Mochilas/', Bolsos_Mochilas, name = 'Bolsos_Mochilas'),
    path('Llaveros/', Llaveros, name = 'Llaveros'),

    path('buscar_productos_indumentarias/', buscar_productos_indumentarias, name = 'buscar_productos_indumentarias'),

]

