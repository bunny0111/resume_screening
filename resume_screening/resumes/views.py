from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status, viewsets
from .models import Resume
from .serializers import ResumeSerializer
from .utils import extract_text, extract_entities


# This function is to Post data manually
'''class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    parser_classes = (MultiPartParser, FormParser)  # Allow file uploads
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''
        
class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    parser_classes = (MultiPartParser, FormParser)  # Handle File Uploads
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            resume = serializer.save()
            text = extract_text(resume.file.path)   # Extract text from the uploaded file
            extracted_data = extract_entities(text) # Get structured resume data
            
            # Update the resume instance with extracted data
            resume.skills = extracted_data['skills']
            resume.experience = extracted_data['experience']
            resume.education = extracted_data['education']
            resume.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
'''
Extract text from uploaded file (extract_text()).
Use AI (spaCy) to analyze skills, experience, and education (extract_entities()).
Update the Resume model with the extracted data.
'''