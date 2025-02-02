from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Jobs
from resumes.models import Resume
from resumes.utils import match_resume_to_job
from .serializers import JobSerializer
from rest_framework.decorators import action

class JobViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    
    @action(detail=True, methods=['get'], url_path='match_resumes')
    def match_resumes(self, request, pk=None):
        '''Find best-matching resumes for a given job.'''
        job = self.get_object() # Get Job by ID
        resumes = Resume.objects.all()
        
        matched_resumes  = []
        for resume in resumes:
            score = match_resume_to_job(resume, job)
            if score > 0.3:     # Only return matches above 30%
                matched_resumes.append({
                    "candidate" :  resume.candidate_name,
                    "match_score" : round(score, 2)
                })
                
        return Response({'jobs':job.title, 'matches':matched_resumes}, status=status.HTTP_200_OK)
    
    
'''
Fetches all resumes and matches them against a job.
Returns only resumes with a match score > 50%.
You can call this API as:
GET http://127.0.0.1:8000/api/jobs/{job_id}/match_resumes/
'''