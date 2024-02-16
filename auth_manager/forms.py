from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class JobSeeker_Registration_Form(UserCreationForm):
    fullname = forms.CharField(max_length=255)
    email = forms.EmailField()
    username = forms.CharField(max_length=255)
    

    class Meta:
        model = CustomUser
        fields = ['fullname', 'email', 'username', 'password1', 'password2']


class Company_Registration_Form(UserCreationForm):
    company_name = forms.CharField(max_length=255)
    fullname = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
   

    class Meta:
        model = CustomUser
        fields = ['company_name', 'fullname', 'username', 'email', 'password1', 'password2']