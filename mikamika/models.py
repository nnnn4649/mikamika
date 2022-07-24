from django.db import models
from django.utils import timezone
import uuid
 

HYOUKA_CHOICES = [
        ('0','soso'),
        ('1','good'),
    ]

class Mikamika(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(verbose_name='日付', default=timezone.now)
    store = models.CharField(verbose_name='店名', max_length=40,default='')
    bikou = models.CharField(verbose_name='一言', max_length=20 , null=True, blank=True,)
    hyouka = models.CharField(verbose_name="評価", choices=HYOUKA_CHOICES, max_length=10, null=True, blank=True,)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)

    def __str__(self):
         return self.store