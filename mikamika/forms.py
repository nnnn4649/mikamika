from django import forms
from .models import Mikamika


class MikamikaForm(forms.ModelForm):
    class Meta:
        model = Mikamika
        fields = ('store','bikou','hyouka','todou')
        widgets = {
            'store' : forms.TextInput(attrs={'class'  : 'form-control'}),
            'bikou' : forms.TextInput(attrs={'class'  : 'form-control'}),
            'hyouka': forms.RadioSelect(attrs={'class': 'form-control'}),
            'todou' : forms.RadioSelect(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        rstore = kwargs.pop('rstore', None)
        rtodou = kwargs.pop('rtodou', None)
        self.base_fields['store'].initial = rstore
        self.base_fields['store'].widget.attrs['readonly'] = 'readonly'
        self.base_fields['todou'].initial = rtodou
        self.base_fields['todou'].widget.attrs['readonly'] = 'readonly'
        super().__init__(*args, **kwargs)
        
        