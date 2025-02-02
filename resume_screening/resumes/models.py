from django.db import models

# Create your models here.
'''class Resume(models.Model):
    candidate_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    skills = models.TextField(blank=True, null=True) # Extracted skills
    experience = models.TextField(blank=True, null=True)  # Extracted experience
    education = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.candidate_name'''
    
# modify the Resume model to store parsed information.
class Resume(models.Model):
    candidate_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    skills = models.JSONField(blank=True, null=True) # Store skills as JSON
    experience = models.JSONField(blank=True, null=True) # Store experience as JSON
    education = models.JSONField(blank=True, null=True) # Store education as JSOn
    file = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.candidate_name
    
# JSONField is used to store structured data like extracted skills, experience, and education.
