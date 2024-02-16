from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['username','email','role']

admin.site.register(CustomUser,CustomUserAdmin)

