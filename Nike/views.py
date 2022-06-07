from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

#from products.models import Products
from Nike.models import indumentarias,calzados,accesorios
from Nike.forms import Indumentarias_form, Calzados_form, Accesorios_form

# Create your views here.
def products(request):
    print(request.method)
    productos = indumentarias.objects.all()
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)


def create_product_view(request):
    if request.method == 'GET':
        form = Indumentarias_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = Indumentarias_form(request.POST,files=request.FILES)
        if form.is_valid():
            new_product = indumentarias.objects.create(
                codigo_barra = form.cleaned_data['codigo_barra'],
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                talle = form.cleaned_data['talle'],
                color = form.cleaned_data['color'],
                cod_estacion = form.cleaned_data['cod_estacion'],
                cod_categoria = form.cleaned_data['cod_categoria'],
                imagen = form.cleaned_data['imagen'],
                #imagen = request.FILES.get('imagen'),
            )
            context ={'new_product':new_product}
        return render(request, 'create_product.html', context=context)

def search_product_view(request):
    print(request.GET)
    #product = Products.objects.get()
    products = indumentarias.objects.filter(name__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'search_product.html', context = context)


def calzado_view(request):
    print(request.method)
    calzado = calzados.objects.all()
    context = {'calzado':calzado}
    return render(request, 'calzado.html', context=context)

def crear_productos_calzados(request):
    if request.method == 'GET':
        form = Calzados_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = Calzados_form(request.POST,files=request.FILES)
        if form.is_valid():
            nuevo_calzado = calzados.objects.create(
                codigo_barra = form.cleaned_data['codigo_barra'],
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                talle = form.cleaned_data['talle'],
                color = form.cleaned_data['color'],
                cod_categoria = form.cleaned_data['cod_categoria'],
                imagen = form.cleaned_data['imagen'],
            )
            context ={'nuevo_calzado':nuevo_calzado}
        return render(request, 'create_product.html', context=context)

def buscar_productos_calzados(request):
    print(request.GET)
    #product = Products.objects.get()
    calzado = calzados.objects.filter(name__contains = request.GET['search'])
    context = {'calzado':calzado}
    return render(request, 'search_product.html', context = context)



def crear_productos_accesorios(request):
    if request.method == 'GET':
        form = Accesorios_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = Accesorios_form(request.POST,files=request.FILES)
        if form.is_valid():
            nuevo_accesorio = accesorios.objects.create(
                codigo_barra = form.cleaned_data['codigo_barra'],
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                color = form.cleaned_data['color'],
                cod_categoria = form.cleaned_data['cod_categoria'],
                imagen = form.cleaned_data['imagen'],
            )
            context ={'nuevo_accesorio':nuevo_accesorio}
        return render(request, 'create_product.html', context=context)

def buscar_productos_accesorios(request):
    print(request.GET)
    #product = Products.objects.get()
    accesorio = accesorios.objects.filter(name__contains = request.GET['search'])
    context = {'accesorio':accesorio}
    return render(request, 'search_product.html', context = context)
