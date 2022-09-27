from django import forms
from .models import CustomUser
from django.contrib.auth.models import User
#from .models import Account
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import UserManager, AbstractUser


class AccountForm(UserCreationForm):
    # パスワード入力：非表示対応
   # password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")
    class Meta(UserCreationForm):
        # ユーザー認証
        model = CustomUser
        # フィールド指定
        fields = UserCreationForm.Meta.fields + ('email','sex','age')

class AddAccountForm(UserChangeForm):
     class Meta():
        # モデルクラスを指定
        model = CustomUser
        fields = UserChangeForm.Meta.fields