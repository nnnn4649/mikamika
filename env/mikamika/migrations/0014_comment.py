# Generated by Django 4.2 on 2023-04-17 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mikamika', '0013_userinfo_create_user_userinfo_todou'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commet', models.CharField(default='', max_length=40, verbose_name='コメント')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mikamika.userinfo', verbose_name='対象店名')),
            ],
        ),
    ]
