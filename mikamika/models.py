from django.db import models
from django.utils import timezone
import uuid
 
 
class Mikamika(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(verbose_name='日付', default=timezone.now)
    store = models.CharField(verbose_name='店名', max_length=40)
    bikou = models.CharField(verbose_name='一言', max_length=40)
    soso = models.BooleanField(initial=0)
    good = models.BooleanField(initial=1)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)