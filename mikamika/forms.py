from django import forms
from .models import Mikamika


class MikamikaForm(forms.ModelForm):
    class Meta:
        model = Mikamika
        fields = ('date', 'title', 'text',)
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }