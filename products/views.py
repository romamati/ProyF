from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

#from products.models import Products
from products.models import indumentarias,calzados,accesorios
from products.forms import Indumentarias_form

# Create your views here.
def products(request):
    print(request.method)
    productos = indumentarias.objects.all()
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

def contacto(request):
    return render(request, 'contacto.html')

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