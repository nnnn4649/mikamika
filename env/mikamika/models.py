from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
import uuid

HYOUKA_CHOICES = [
        ('0','soso'),
        ('1','good'),
    ]

TODOU_CHOICES = [
        ('0','tokyo'),
        ('1','oosaka'),
        ('2','kyouto'),
    ]

class Mikamika(models.Model):   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,default='',)
    date = models.DateField(verbose_name='日付', default=timezone.now)
    store = models.CharField(verbose_name='店名', max_length=40,default='')
    bikou = models.CharField(verbose_name='一言', max_length=20 , null=True, blank=True,)
    hyouka = models.CharField(verbose_name="評価", choices=HYOUKA_CHOICES, max_length=10, null=True, blank=True,)
    todou = models.CharField(verbose_name="都道府県", choices=TODOU_CHOICES, max_length=10, null=True, blank=True,)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='img/')

    def __str__(self):
         return self.create_user.username

class UserInfo(models.Model):
      create_user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,default='',)
      userstore = models.CharField(verbose_name='ユーザー店名', max_length=40,default='',unique=True)
      todou = models.CharField(verbose_name="都道府県", choices=TODOU_CHOICES, max_length=10, null=True, blank=True,)
      usersubject = models.CharField(verbose_name='タイトル', max_length=20 , null=True, blank=True,)
      review = models.CharField(verbose_name='レビュー', max_length=200,default='')

      def __str__(self):
         return str(self.userstore)
      
class Comment(models.Model):
      create_user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,default='',)
      target = models.ForeignKey(UserInfo, to_field="userstore",on_delete=models.CASCADE, verbose_name='対象店名')
      commet = models.CharField(verbose_name='コメント', max_length=40,default='')
      created_at = models.DateTimeField(verbose_name='コメント日時', default=timezone.now)

      def __str__(self):
         return str(self.target)

     