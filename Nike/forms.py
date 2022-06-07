from django import forms
from Nike.models import indumentarias,calzados,accesorios

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