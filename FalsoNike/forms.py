from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import User_profile




class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
        #Saca los mensajes de ayuda
        help_texts = {k:'' for k in fields}

class User_profile_form(forms.ModelForm):
    photo = forms.FileField(label='Photo', widget=forms.FileInput())

    class Meta:
        model = User_profile
        fields = ['photo']
        help_texts = {k:'' for k in fields}
