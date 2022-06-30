from django.urls import path

from Nike.views import sobre_nosotros,Detalle_accesorios, Detalle_indumentarias, Detalle_calzado, Eliminar_indumentarias, Eliminar_accesorios, Eliminar_calzado,Editar_accesorios, Editar_indumentarias, Editar_calzado,buscar_productos_indumentarias,Pelota,Pulseras,Cantiplora,Anteojos,Muñequeras,Bolsos_Mochilas,Llaveros,Remeras,Camperas,Pantalones,Buzos,crear_productos_indumentarias,crear_productos_calzados,crear_productos_accesorios,calzado_view,indumentaria_view,accesorio_view,ZapatillaDeportiva,ZapatillaComunes,Botines,Ojotas

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

    path('calzado-detalle/<int:pk>/',Detalle_calzado.as_view(), name='calzado-detalle'),
    path('accesorios-detalle/<int:pk>/',Detalle_accesorios.as_view(), name='accesorios-detalle'),
    path('indumentarias-detalle/<int:pk>/',Detalle_indumentarias.as_view(), name='indumentarias-detalle'),
    path('calzado-eliminar/<int:pk>/',Eliminar_calzado.as_view(), name='calzado-eliminar'),
    path('indumentarias-eliminar/<int:pk>/',Eliminar_indumentarias.as_view(), name='indumentarias-eliminar'),
    path('accesorios-eliminar/<int:pk>/',Eliminar_accesorios.as_view(), name='accesorios-eliminar'),
    path('calzado-editar/<int:pk>/',Editar_calzado.as_view(), name='calzado-editar'),
    path('accesorios-editar/<int:pk>/',Editar_accesorios.as_view(), name='accesorios-editar'),
    path('indumentarias-editar/<int:pk>/',Editar_indumentarias.as_view(), name='indumentarias-editar'),

    path('buscar_productos_indumentarias/', buscar_productos_indumentarias, name = 'buscar_productos_indumentarias'),

    path('sobre_nosotros/',sobre_nosotros, name = 'sobre_nosotros')

]

