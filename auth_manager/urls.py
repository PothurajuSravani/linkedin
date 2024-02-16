from django.urls import path
from .views import login_user,company_registration,job_seeker_registration,home_page


urlpatterns = [
    path('',home_page,name='home-page'),
   
    path('login/', login_user, name='login_user'),
    path('company/', company_registration, name='company_registration'),
    path('job/', job_seeker_registration, name='job_seeker_registration'),
    
]



