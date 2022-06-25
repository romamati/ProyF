from django import forms
from Nike.models import indumentarias,calzados,accesorios
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class Product_form(forms.Form):
#     name = forms.CharField(max_length=40)
#     price = forms.FloatField()
#     description = forms.CharField(max_length=200)
#     SKU = forms.CharField(max_length=30)
#     active = forms.BooleanField()

class Indumentarias_form(forms.ModelForm):
    class Meta:
        model = indumentarias
        fields = '__all__'

class Calzados_form(forms.ModelForm):
    class Meta:
        model = calzados
        fields = '__all__'

class Accesorios_form(forms.ModelForm):
    class Meta:
        model = accesorios
        fields = '__all__'

#class User_registration_form(UserCreationForm):
   # email = forms.EmailField()
   # password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
   # password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)

    #class Meta:
    #    model = User
    #    fields = ['username', 'email', 'password1', 'password2']
    #    help_texts = {k:'' for k in fields}