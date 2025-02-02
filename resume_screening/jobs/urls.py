from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet)    # Automatically registers all endpoints

urlpatterns = [
    path('', include(router.urls)),
    # path('jobs/<int:pk>/match_resumes/', JobViewSet.as_view({'get': 'match_resumes'}), name='job-match-resumes'),
]

'''
DefaultRouter: Automatically generates the routes for CRUD operations for your JobViewSet.
match_resumes: Adds a custom URL route to the JobViewSet for matching resumes to a job based on the pk (primary key) of the job.
path('jobs/<int:pk>/match_resumes/'): This URL captures the job ID and links it to the match_resumes method that returns matching resumes for a specific job.
'''