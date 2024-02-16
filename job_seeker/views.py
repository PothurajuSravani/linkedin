from django.shortcuts import render, redirect
from company.models import JobPosting
from django.contrib.auth.decorators import login_required
from .forms import JobSeekerForm, JobApplicationForm
from .models import  JobSeeker,JobApplication
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from company.forms import JobPostingForm
from company.views import create_job_posting
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notification




@login_required
def job_seeker_dashboard(request):
    posts = JobPosting.objects.all().order_by('-posted_on')
    return render (request,'job_seeker_dashboard.html',{'posts':posts})



@login_required
def read_post(request, pk):
    post = JobPosting.objects.get(pk=pk)
    post.views += 1
    post.save()
    jobseeker = JobSeeker.objects.get(user=request.user)
    applied = JobApplication.objects.filter(
        applicant=jobseeker, job=post).exists()
    return render(request, 'read_post.html', {'post': post, 'applied': applied})


@login_required
def job_seeker_form(request):
    if request.method == 'POST':
        form = JobSeekerForm(request.POST, request.FILES)
        if form.is_valid():
            jobseeker = form.save(commit=False)
            jobseeker.user = request.user
            jobseeker.save()
            return redirect('job_seeker_profile')  
    else:
        form = JobSeekerForm()

    return render(request, 'job_seeker_form.html', {'form': form})

@login_required
def update_jobseeker_form(request):
    jobseeker = JobSeeker.objects.get(user=request.user)

    if request.method == 'POST':
        form = JobSeekerForm(request.POST, request.FILES, instance=jobseeker)
        if form.is_valid():
            form.save()
            return redirect('job_seeker_profile') 
    else:
        form = JobSeekerForm(instance=jobseeker)

    return render(request, 'update_job_seeker_form.html', {'form': form})


@login_required
def job_application_form(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.applicant = JobSeeker.objects.get(user=request.user)  # Assuming the user is a job seeker
            job_application.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = JobApplicationForm()

    return render(request,'job_applications.html', {'form': form})

@login_required
def job_seeker_profile(request):
    job_seekers = JobSeeker.objects.filter(user=request.user)
    if job_seekers.exists():
        job_seeker = job_seekers.first()  # or any logic to choose one from multiple results
        return render(request, 'job_seeker_profile.html', {'job_seeker': job_seeker})
    else:
        # Handle the case when no JobSeeker is found
        return redirect('job_seeker_form')

@login_required
def update_job_seeker_form(request):
    jobseeker = JobSeeker.objects.get(user=request.user)

    if request.method == 'POST':
        form = JobSeekerForm(request.POST, request.FILES, instance=jobseeker)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = JobSeekerForm(instance=jobseeker)

    return render(request, 'update_job_seeker_form.html', {'form': form})


@api_view(['POST'])
@login_required
def apply_job(request, post_pk):
    try:
        job_posting = get_object_or_404(JobPosting, pk=post_pk)

        if not request.user.is_authenticated:
            return Response({'status': 'error', 'message': 'Authentication required'}, status=401)

        job_seeker = JobSeeker.objects.get(user=request.user)

        existing_application = JobApplication.objects.filter(
            job=job_posting, applicant=job_seeker).exists()

        if existing_application:
            return Response({'status': 'error', 'message': 'You have already applied for this job'}, status=400)

        job_application = JobApplication.objects.create(
            job=job_posting, applicant=job_seeker)
        return Response({'status': 'success'})

    except Exception as e:

        return Response({'status': 'error', 'message': str(e)}, status=500)
    

# jobseeker/views.py
from .models import Notification

def notification_page(request):
    user = request.user
    notifications = Notification.objects.filter(user=user)
    return render(request, 'notification_page.html', {'notifications': notifications})




