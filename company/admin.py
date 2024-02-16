from django.contrib import admin

# Register your models here.

from .models import Company,JobPosting

admin.site.register(Company)
admin.site.register(JobPosting)
