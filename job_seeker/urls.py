from django.urls import path
from .import views

urlpatterns = [
    path('jobseekerdashboard/',views.job_seeker_dashboard,name='job_seeker_dashboard'),
    path('readposts/<int:pk>',views.read_post,name='readposts'),
    path('job-seeker-form/', views.job_seeker_form, name='job_seeker_form'),
    path('job_applications/<int:post_id>/', views.job_application_form, name='job_application_form'),
    path('job-seeker-profile/', views.job_seeker_profile, name='job_seeker_profile'),
    path('update_job_seeker_form/', views.update_job_seeker_form, name='update_jobseeker'),
    path('apply_job/<int:post_pk>/', views.apply_job, name='apply_job'),
    # path('notifications/', views.notification_list, name='notification_list'),
    # path('notifications/mark_as_read/<int:notification_id>/',views.mark_as_read, name='mark_as_read'),
    path('notifications/', views.notification_page, name='notification-page'),
    

]