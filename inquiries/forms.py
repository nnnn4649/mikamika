from django import forms
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):
 name = forms.CharField(label='お名前', max_length=30)
 email = forms.EmailField(label='メール')
 inquiry = forms.CharField(label='問い合わせ内容',widget=forms.Textarea)
   
 def __init__(self, *args, **kwargs):
   super().__init__(*args, **kwargs)

 def send_email(self):
    name = self.cleaned_data['name']
    email = self.cleaned_data['email']
    inquiry = self.cleaned_data['inquiry']
    
    message = EmailMessage(subject=name + "からの問い合わせ",
                            body=inquiry,
                            from_email=email,
                            to=["nakagawa.nihonest@gmail.com"],
                            cc=[email])
    message.send()