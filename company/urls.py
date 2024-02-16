from django.urls import path
from .import views


urlpatterns = [
    path('hrdashboard/',views.hr_dashboard,name='hr-dashboard'),
    path('create_post/',views.create_job_posting,name='create_job_posting'),
    path('read_post/<int:pk>',views.read_post_page,name='read-page'),
    path('my_posts/', views.my_posts, name='my-posts'),
    path('company_list/', views.company_list, name='company-list'),
    path('company/update_company/<int:company_id>/',views.update_company, name='update-company'),
    path('company/update_job_posting/<int:pk>/', views.update_job_posting, name='update-job-posting'),
    path('company/delete_job_posting/<int:pk>/', views.delete_job_posting, name='delete-job-posting'),
    # urls.py
    path('company/applied_jobseekers/<int:job_posting_id>/', views.applied_jobseekers, name='applied_jobseekers'),
    # path('hire/<int:job_posting_id>/<int:job_seeker_id>/', views.hire_jobseeker,name='hire_job_seeker'),
     path('hire_jobseeker/', views.hire_jobseeker, name='hire-jobseeker'),
]


