from django.db import models
from auth_manager.models import CustomUser
from company.models import JobPosting



# Create your models here.
class JobSeeker(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='job_seekers')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,null=True,blank=True)
    bio = models.TextField(blank=True,null=True)
    skills = models.TextField()
    experience = models.TextField(blank=True,null=True)
    education = models.TextField()
    resume = models.FileField(upload_to='resume/',null=True,blank=True)

    def __str__(self):
        return self.name
    
class JobApplication(models.Model):
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    applicant = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)
    
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('hired', 'Hired'),
        # Add more status choices as needed
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='applied')
    
    def __str__(self):
        return f"{self.applicant.user.username} - {self.job.title} - {self.status}"

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message}"