from django.db import models

# Store Job descriptions in the database
class Jobs(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    required_skills = models.JSONField()    # store skills as JSON
    experience_required = models.IntegerField(default=0) # Years of experience
    
    def __str__(self):
        return self.title
    
'''
Stores job title, company name, and description.
required_skills: JSON field to store required skills.
experience_required: Years of experience needed for the job.
'''