import spacy
import re
from pdfminer.high_level import extract_text
from lists import skills_list, education_keywords

nlp = spacy.load('en_core_web_lg')

def extract_contact(text):
    contact_number = None
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    if match:
        contact_number = match.group()
    return contact_number

def extract_email(text):
    email = None
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    if match:
        email = match.group()
    return email

def extract_skills(text, skills_list=skills_list):
    skills = []
    for skill in skills_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            skills.append(skill)

    return skills

def extract_education(text, education_keywords=education_keywords):
    education = []

    for keyword in education_keywords:
        pattern = r"(?i)\b{}\b".format(re.escape(keyword))
        match = re.search(pattern, text)
        if match:
            education.append(match.group())

    return education

def extract_name(text):
    name = None
    pattern = r"(\b[A-Z]+\b)\s(\b[A-Z]+\b)"
    match = re.search(pattern, text)
    if match:
        name = match.group()
    else:
        pattern = r"(\b[A-Z][a-z]+\b)\s(\b[A-Z][a-z]+\b)"
        match = re.search(pattern, text)
        if match: 
            name = match.group()

    return name

# resume_path = "Resume2.pdf"
# text = extract_text(resume_path)

