from django import forms
from Nike.models import indumentarias,calzados,accesorios,Avatar
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsersFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = '__all__'
