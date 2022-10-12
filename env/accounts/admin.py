from django.contrib import admin

# Register your models here.
from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from accounts.forms import AccountForm, AddAccountForm


# Register your models here.
class CustomUserAdmin(UserAdmin):
  add_form = AccountForm
  form = AddAccountForm
  model = CustomUser
  list_display = ['email', 'username', 'sex', 'age',]
  list_editable = ['sex','age',]

admin.site.register(CustomUser, CustomUserAdmin)