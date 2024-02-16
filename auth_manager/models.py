from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.




class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('job_seeker','JobSeeker'),
        ('company_hr','Company Hr')
    ]
    role = models.CharField(max_length=255, choices = ROLE_CHOICES)
    fullname = models.CharField(max_length=225,default='')