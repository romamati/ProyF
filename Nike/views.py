from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Nike.models import indumentarias,calzados,accesorios,Avatar
from Nike.forms import Indumentarias_form, Calzados_form, Accesorios_form

from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse

#--------------------INFO DE LA WEB Y LOS CREADORES---------------------------
def sobre_nosotros(request):
    return render(request, 'Sobre_mi.html')

#--------------------------------------Parte de Indumentarias--------------------------------------------------------------
def indumentaria_view(request):
    print(request.method)
    productos = indumentarias.objects.all()
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

def crear_productos_indumentarias(request):
    if request.method == 'GET':
        form = Indumentarias_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = Indumentarias_form(request.POST,files=request.FILES)
        if form.is_valid():
            nuevo_indumentaria = indumentarias.objects.create(
                codigo_barra = form.cleaned_data['codigo_barra'],
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                talle = form.cleaned_data['talle'],
                color = form.cleaned_data['color'],
                #cod_categoria = form.cleaned_data['cod_categoria'],
                imagen = form.cleaned_data['imagen'],
                categoria = form.cleaned_data['categoria'],
            )
            context ={'nuevo_indumentaria':nuevo_indumentaria}
        return render(request, 'create_product.html', context=context)

def Remeras(request):
    print(request.method)
    productos = indumentarias.objects.filter(categoria = 1)
    #productos = indumentarias.objects.all().select_related('Categoria_Indumentaria').filter(name='Remeras')
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

def Pantalones(request):
    print(request.method)
    productos = indumentarias.objects.filter(categoria = 2)
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

def Camperas(request):
    print(request.method)
    productos = indumentarias.objects.filter(categoria = 3)
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

def Buzos(request):
    print(request.method)
    productos = indumentarias.objects.filter(categoria = 4)
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

#--------------------------------------Parte de Calzados--------------------------------------------------------------
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
                #cod_categoria = form.cleaned_data['cod_categoria'],
                imagen = form.cleaned_data['imagen'],
                categoria = form.cleaned_data['categoria'],
            )
            context ={'nuevo_calzado':nuevo_calzado}
        return render(request, 'create_product.html', context=context)

def ZapatillaDeportiva(request):
    print(request.method)
    productos = calzados.objects.filter(categoria = 1)
    #productos = calzados.objects.all().select_related('Categoria_Calzados').filter(name='Remeras')
    context = {'productos':productos}
    return render(request, 'calzado.html', context=context)

def ZapatillaComunes(request):
    print(request.method)
    productos = calzados.objects.filter(categoria = 2)
    context = {'productos':productos}
    return render(request, 'calzado.html', context=context)

def Botines(request):
    print(request.method)
    productos = calzados.objects.filter(categoria = 3)
    context = {'productos':productos}
    return render(request, 'calzado.html', context=context)

def Ojotas(request):
    print(request.method)
    productos = calzados.objects.filter(categoria = 4)
    context = {'productos':productos}
    return render(request, 'calzado.html', context=context)

#--------------------------------------Parte de Accesorios--------------------------------------------------------------
def accesorio_view(request):
    print(request.method)
    accesorio = accesorios.objects.all()
    context = {'accesorio':accesorio}
    return render(request, 'accesorio.html', context=context)

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
                #cod_categoria = form.cleaned_data['cod_categoria'],
                imagen = form.cleaned_data['imagen'],
                categoria = form.cleaned_data['categoria'],
            )
            context ={'nuevo_accesorio':nuevo_accesorio}
        return render(request, 'create_product.html', context=context)

def Pelota(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 1)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Pulseras(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 2)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Cantiplora(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 3)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Anteojos(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 4)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Muñequeras(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 5)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Bolsos_Mochilas(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 6)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Llaveros(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 7)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

#------------------------------BUSQUEDA GENERAL--------------------------------
def buscar_productos_indumentarias(request):
    productos = []
    producto_search = indumentarias.objects.filter(nombre__contains=request.GET["search"])
    calzado_search = calzados.objects.filter(nombre__contains=request.GET["search"])
    accesorio_search = accesorios.objects.filter(nombre__contains=request.GET["search"])
    for x in producto_search:
        productos.append(x)
    for x in calzado_search:
        productos.append(x)
    for x in accesorio_search:
        productos.append(x)
    if productos:
        context = {"productos": productos}
    else:
        context = {"errors": "No se encontro el producto"}
    return render(request, "search_product.html", context=context)


class Detalle_calzado(DetailView):
    model= calzados
    template_name= 'calzado_detalle.html'

class Detalle_indumentarias(DetailView):
    model= indumentarias
    template_name= 'indumentarias_detalle.html'

class Detalle_accesorios(DetailView):
    model= accesorios
    template_name= 'accesorios_detalle.html'

class Eliminar_calzado(DeleteView):
    model= calzados
    template_name= 'calzado_eliminar.html'

    def get_success_url(self):
        return reverse ('ZapatillaDeportiva')

class Eliminar_indumentarias(DeleteView):
    model= indumentarias
    template_name= 'indumentarias_eliminar.html'

    def get_success_url(self):
        return reverse ('Indumentarias')

class Eliminar_accesorios(DeleteView):
    model= accesorios
    template_name= 'accesorios_eliminar.html'

    def get_success_url(self):
        return reverse ('Accesorios')

class Editar_calzado (UpdateView):
    model= calzados
    template_name= 'calzado_editar.html'
    fields= '__all__'

    def get_success_url(self):
        return reverse ('Calzados')

class Editar_indumentarias (UpdateView):
    model= indumentarias
    template_name= 'indumentarias_editar.html'
    fields= '__all__'

    def get_success_url(self):
        return reverse ('Indumentarias')

class Editar_accesorios (UpdateView):
    model= accesorios
    template_name= 'accesorios_editar.html'
    fields= '__all__'

    def get_success_url(self):
        return reverse ('Accesorios')