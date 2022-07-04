from datetime import datetime


from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime  import datetime

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from FalsoNike.forms import User_registration_form,User_profile_form


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #context = {'message':f'Bienvenido {username}!! :D'}
                return redirect('/')#redireccionar mi vista
            else:
                context = {'errors':'No hay ningun usuario con esas credenciales!!!'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/login.html', context = context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context = context)


def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        form1 = User_profile_form(request.POST)

        if form.is_valid() and form1.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            form1.save()
            photo = form.cleaned_data['photo']
            user = authenticate(username = username, password = password, first_name=first_name, last_name=last_name,photo=photo)
            login(request, user)
            context = {'message':f'Usuario creado correctamente, bienvenido {username}'}
            return render(request, 'index.html', context = context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context = context)
    else:
        form = User_registration_form()
        form1 = User_profile_form()
        #form1 = User_profile_form()
        context = {'form':form,'form1':form1}
        return render(request, 'auth/register.html', context =context)



def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.user.is_authenticated and request.user.is_superuser:
       print(request.user.username)
       return render(request, 'contact.html')
    else:
        return redirect('login')



