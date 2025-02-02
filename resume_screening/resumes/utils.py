# This file is for handling text extraction
import fitz #PyMuPDF
import docx

def extract_text_from_pdf(pdf_path):
    '''Extract text from a PDF file'''
    text = ''
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text('text') + '\n'
    return text

def extract_text_from_docx(docx_path):
    '''Extract text from a docx file'''
    text = ''
    doc = docx.Document(docx_path)
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text

def extract_text(file_path):
    '''Determine file type and extract text accordingly'''
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    return ""

'''
extract_text_from_pdf(): Reads text from each page of a PDF.
extract_text_from_docx(): Reads paragraphs from a DOCX file.
extract_text(): Detects file type and calls the appropriate function.
'''

# extract skills, experience, and education using spaCy NLP.

import spacy
nlp = spacy.load('en_core_web_sm')  # Load the spaCy model

def extract_entities(text):
    '''Extract education, skills, experience from resume text'''
    doc = nlp(text)
    skills = []
    experience = []
    education = []
    
    for ent in doc.ents:
        if ent.label_ in ['ORG', 'EDUCATION']:  # Education-related entities
            education.append(ent.text)
        elif ent.label_ in ['DATE', 'TIME']:    # Experience-related entities
            experience.append(ent.text)
        elif ent.label_ in ['GPE', 'PRODUCT']:  # Skills-related entities
            skills.append(ent.text)
            
    return {
        'skills': list(set(skills)),
        'experience': list(set(experience)),
        'education': list(set(education))
    }
    
    
'''
We load spaCy's NLP model (en_core_web_sm).
We scan the resume text for:
    Education (ORG, EDUCATION labels)
    Experience (DATE, TIME labels)
    Skills (GPE, PRODUCT labels) (basic approach, later we can use AI models for accuracy)
'''

# use BERT for skill extraction.
'''
BERT, short for Bidirectional Encoder Representations from Transformers, is a machine learning (ML) framework for natural language processing.
'''
from transformers import pipeline

# Load pre-trained AI model
nlp_bert = pipeline('ner', model="dbmdz/bert-large-cased-finetuned-conll03-english")

def extract_advanced_entites(text):
    '''Use AI to extract skills, experience, and education from resumes.'''
    results = nlp_bert(text)
    skills = []
    experience = []
    education = []
    
    for entity in results:
        word = entity['word']
        entity_type = entity['entity']
        
        if entity_type in ['B-ORG', 'I-ORG']:   # Organizations(Education)
            education.append(word)
        elif entity_type in ['B-MISC', 'I-MISC']: # Skills
            skills.append(word)
        elif entity_type in ['B-DATE', 'I-DATE']: # Experience related data
            experience.append(word)
            
    return {
        "skills" : list(set(skills)),
        "experience" : list(set(experience)),
        "education" : list(set(education))
    }
    
'''Uses BERT (dbmdz/bert-large-cased) for Named Entity Recognition (NER).
Extracts skills, experience, and education with higher accuracy than spaCy.
Can recognize complex skills like "Machine Learning", "Python Programming", etc.'''

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2') # Load AI model for text similarity

def match_resume_to_job(resume, job):
    '''Match a resume to a job based on skills and experience using AI similarity.'''
    
    # Ensure skills and experience are lists and not None
    resume_skills = resume.skills if resume.skills else []
    resume_experience = resume.experience if resume.experience else []
    job_skills = job.required_skills if job.required_skills else []
    
    # convert to strings
    resume_text = " ".join(resume.skills or [""]) + " " + " ".join(resume.experience or [""])
    job_text = " ".join(job.required_skills or [""]) + f" {job.experience_required} years experience"
    
    # Generate AI embeddings
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_text, convert_to_tensor=True)
    
    # Calculate similarity score (0 to 1)
    similarity_score = util.pytorch_cos_sim(resume_embedding, job_embedding).item()
    
    return round(similarity_score, 2) # Return match percentage

'''
Uses Sentence-BERT (all-MiniLM-L6-v2) to compare resume & job descriptions.
Generates AI embeddings for resume skills & experience vs. job requirements.
Calculates a similarity score (0-1), where 1 = perfect match.
'''