# Generated by Django 4.0.6 on 2022-07-26 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mikamika', '0004_mikamika_todou'),
    ]

    operations = [
        migrations.AddField(
            model_name='mikamika',
            name='create_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
