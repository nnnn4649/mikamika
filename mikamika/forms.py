from django import forms
from .models import Mikamika


class MikamikaForm(forms.ModelForm):
    class Meta:
        model = Mikamika
        fields = ('store','bikou','hyouka','todou')
        widgets = {
            'store' : forms.TextInput(attrs={'class': 'form-control'}),
            'bikou' : forms.TextInput(attrs={'class': 'form-control'}),
            'hyouka': forms.RadioSelect(attrs={'class': 'form-control'}),
            'todou' : forms.RadioSelect(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        self.base_fields['store'].widget.attrs['readonly'] = 'readonly'
        self.base_fields['bikou'].initial = '1000'
        super().__init__(*args, **kwargs)
        
        