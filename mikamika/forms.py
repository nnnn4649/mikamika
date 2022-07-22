from django import forms
from .models import Mikamika


class MikamikaForm(forms.ModelForm):
    class Meta:
        model = Mikamika
        fields = ('store', 'bikou','hyouka')
        widgets = {
            'store' : forms.TextInput(attrs={'class': 'form-control'}),
            'bikou' : forms.TextInput(attrs={'class': 'form-control'}),
            'hyouka': forms.RadioSelect(attrs={'class': 'form-control'}),
        }
    