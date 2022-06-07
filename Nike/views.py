from django.shortcuts import render
from Nike.models import indumentarias,calzados,accesorios
# Create your views here.


#def producto_add(request):
#    producto_nuevo = indumentarias.objects.create(
#        codigo_barra = '123',
#        nombre = 'Remera',
#        precio = 10,
#        talle = 's',
#        color = 'rojo',
#        cod_estacion = 1
#        )
#    context = {'producto_nuevo':producto_nuevo}
#    return render(request,'index.html',context=context)


def producto_add(request):
    producto_nuevo = indumentarias.objects.all()
    context = {'producto_nuevo':producto_nuevo}
    return render(request,'base.html',context=context)

def indumentaria(request):
    producto_nuevo = indumentarias.objects.all()
    context = {'producto_nuevo':producto_nuevo}
    return render(request, 'index.html',context=context)


