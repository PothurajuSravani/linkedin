from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import JobSeeker_Registration_Form,Company_Registration_Form
from .models import CustomUser
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from company.models import Company


def home_page(request):
    return render(request,'home.html')

# JobSeeker Registration View
def job_seeker_registration(request):
    if request.method == 'POST':
        form = JobSeeker_Registration_Form(request.POST)
        
        if form.is_valid():
            cleaned_data = form.cleaned_data
            job_seeker = CustomUser.objects.create(
                fullname=cleaned_data['fullname'],
                email=cleaned_data['email'],
                username=cleaned_data['username'],
                password=make_password(cleaned_data['password1']),
                role='job_seeker'
            )

            # Send welcome email
            subject = 'Welcome to Your Website'
            message = 'welcome_email'
            from_email = "sravanipothuraju991@gmail.com"
            recipient_list = [job_seeker.email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=True)
            
            messages.success(request, 'Job Seeker Registration Successful. Welcome email sent.')
            job_seeker.save()
            
            messages.success(request, 'Job Seeker Registration Successful')
            return redirect('login_user')
            
        else:
            messages.error(request, 'Registration failed. Please check the form.')
    else:
        form = JobSeeker_Registration_Form()

    return render(request, 'jobseeker.html', {'form': form})
    
#Company Registration View
def company_registration(request):
    if request.method == 'POST':
        form = Company_Registration_Form(request.POST)
        if form.is_valid():
            data = form.data
            new_user = CustomUser.objects.create(
                fullname = data['fullname'],
                username = data['username'],
                password=make_password(data['password1']),
                email = data['email'],
                role = 'company_hr'
            )

            new_user.save()
            messages.success(request,'Hr registration successful')

            new_company = Company.objects.create(
                name = data['company_name'],
                company_hr = new_user
            )
            new_company.save()
            messages.success(request, 'Company registration successful!')

            # Send welcome email to the company
            subject = 'Welcome to Your Company'
            message = 'welcome_company_email'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [new_user.email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            return redirect('login_user')  
    else:  
        form = Company_Registration_Form()

    return render(request, 'company_reg.html', {'form': form})

#Common Login View
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,'Login Successful')

            if user.role == 'job_seeker':
                return redirect('job_seeker_dashboard')
            elif user.role == 'company_hr':
                return redirect('hr-dashboard')
    else:
        form = AuthenticationForm()
    return render(request,'login_user.html',{'form':form})


#Logout view
def logout_user(request):
    logout(request)
    messages.success(request,'logout Successful')
    return redirect('home_page')



