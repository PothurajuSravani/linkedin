# Generated by Django 5.0.1 on 2024-02-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_manager', '0002_customuser_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('job_seeker', 'JobSeeker'), ('company_hr', 'Company Hr')], max_length=255),
        ),
    ]
