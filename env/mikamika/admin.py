from django.contrib import admin
from .models import Mikamika
from .models import UserInfo
from .models import Comment

#class CommentAdmin(admin.ModelAdmin):
 #   list_display = ('userstore', 'commet')
 
admin.site.register(Mikamika)
admin.site.register(UserInfo)
admin.site.register(Comment)