# Generated by Django 5.0.1 on 2024-02-09 06:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_jobposting_views'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company_description',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='company',
            name='company_hr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hr_of_company', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]