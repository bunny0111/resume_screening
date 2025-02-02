# Resume Matching API

This API provides functionality to match resumes to job descriptions based on skills and experience. It allows recruiters to find the best-matching resumes for a given job posting by comparing the job requirements with the resumes.

## Features

- **Job Matching**: Match resumes to jobs based on skills, experience, and education.
- **Resume Parsing**: Parse resumes (in DOCX/PDF format) to extract relevant information such as skills, experience, and education.
- **Resume Ranking**: Rank and filter resumes based on the match score.

## Setup

### Prerequisites

- Python 3.8+
- Django 3.x or higher
- Django REST Framework
- spaCy (for text extraction and entity recognition)
- BERT or Sentence-Transformers (for advanced skill matching)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   
2. Create a virtual environment (optional but recommended):
    python3 -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\Scripts\activate     # For Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Install the necessary libraries for text extraction:
For spaCy, you need to install the English language model:
   python -m spacy download en_core_web_sm

5. python -m spacy download en_core_web_sm
   python manage.py migrate

6. Create a superuser to access the admin interface (optional):
   python manage.py createsuperuser

7. Run the development server:
   python manage.py runserver

The API will be available at http://127.0.0.1:8000/.

Endpoints
  GET /api/jobs/: Get a list of all job postings.
  GET /api/jobs/{id}/match_resumes/: Get resumes that match the given job posting.

Testing with Postman
  GET Job Matches:
    URL: http://127.0.0.1:8000/api/jobs/{id}/match_resumes/
  Method: GET
    Returns: A list of resumes that match the given job posting based on skills, experience, and education.
Project Structure
  app/: Contains the main Django application.
  app/models.py: Defines models for Job and Resume.
  app/views.py: Contains view logic for handling job and resume matching.
  app/serializers.py: Serializers for Job and Resume models.
  app/urls.py: Contains URL routing.
  requirements.txt: Lists project dependencies.
