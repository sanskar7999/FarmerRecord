from django import forms
from .models import Farm
from django.core import validators


class tractor_details(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['name' , 'email' , 'phone' ,'tractor_brand' , 'model', 'tractor_implements' ]
    
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'phone' : forms.NumberInput(attrs={'class': 'form-control'}),
            'tractor_brand' : forms.TextInput(attrs={'class': 'form-control'}),
            'model' : forms.TextInput(attrs={'class': 'form-control'}),
            'tractor_implements' : forms.Select(attrs={'class': 'form-control'}),

        }
        