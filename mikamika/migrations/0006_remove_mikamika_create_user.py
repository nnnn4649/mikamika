# Generated by Django 4.0.6 on 2022-07-26 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mikamika', '0005_mikamika_create_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mikamika',
            name='create_user',
        ),
    ]
