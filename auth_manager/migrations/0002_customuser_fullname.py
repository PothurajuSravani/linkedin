# Generated by Django 5.0.1 on 2024-02-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='fullname',
            field=models.CharField(default='', max_length=225),
        ),
    ]
