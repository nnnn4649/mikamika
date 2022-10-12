# Generated by Django 4.0.6 on 2022-08-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mikamika', '0008_alter_mikamika_create_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mikamika',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mikamika',
            name='todou',
            field=models.CharField(blank=True, choices=[('0', 'tokyo'), ('1', 'oosaka'), ('2', 'kyouto')], max_length=10, null=True, verbose_name='都道府県'),
        ),
    ]
