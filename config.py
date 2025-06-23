import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
QWEN_API_KEY = os.getenv('QWEN_API_KEY', 'hf_demo')
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-7B-Instruct"

# App Configuration
APP_TITLE = "Career Shift to Future STEM Industry"
APP_ICON = "🚀"
VERSION = "1.0.0"

# Course Data
STEM_FIELDS = {
    'AI & Machine Learning': {
        'icon': '🤖',
        'growth': '+150%',
        'description': 'Transform industries with AI',
        'avg_salary': 130000,
        'courses': [
            'Introduction to Machine Learning',
            'Deep Learning Fundamentals',
            'Natural Language Processing',
            'Computer Vision',
            'AI Ethics and Governance'
        ]
    },
    'Data Science': {
        'icon': '📊',
        'growth': '+120%',
        'description': 'Extract insights from data',
        'avg_salary': 115000,
        'courses': [
            'Data Analysis with Python',
            'Statistical Modeling',
            'Big Data Technologies',
            'Data Visualization',
            'Business Analytics'
        ]
    },
    'Cybersecurity': {
        'icon': '🔒',
        'growth': '+100%',
        'description': 'Protect digital assets',
        'avg_salary': 95000,
        'courses': [
            'Network Security',
            'Ethical Hacking',
            'Digital Forensics',
            'Security Architecture',
            'Incident Response'
        ]
    },
    'Cloud Computing': {
        'icon': '☁️',
        'growth': '+180%',
        'description': 'Scale applications globally',
        'avg_salary': 120000,
        'courses': [
            'AWS Fundamentals',
            'Azure Administration',
            'Google Cloud Platform',
            'DevOps Practices',
            'Kubernetes Management'
        ]
    },
    'Biotechnology': {
        'icon': '🧬',
        'growth': '+80%',
        'description': 'Innovate in life sciences',
        'avg_salary': 85000,
        'courses': [
            'Bioinformatics',
            'Genetic Engineering',
            'Pharmaceutical Development',
            'Biomedical Devices',
            'Regulatory Affairs'
        ]
    }
}

# Skill Categories for Assessment
SKILL_CATEGORIES = {
    "Programming": {
        "skills": ["Python", "R", "SQL", "JavaScript", "Java", "C++"],
        "weight": 0.3
    },
    "Data Analysis": {
        "skills": ["Statistics", "Excel", "Tableau", "Power BI", "Pandas", "NumPy"],
        "weight": 0.25
    },
    "Technical": {
        "skills": ["Git", "Linux", "AWS", "Docker", "APIs", "Databases"],
        "weight": 0.25
    },
    "Soft Skills": {
        "skills": ["Problem Solving", "Communication", "Project Management", "Leadership", "Teamwork"],
        "weight": 0.2
    }
}

# Career Advice Prompts
CAREER_PROMPTS = {
    "transition": """You are a career advisor specializing in STEM transitions. 
    Help professionals transition from traditional careers to STEM fields.
    Focus on practical steps, skill development, and realistic timelines.""",
    
    "skills": """You are a skills assessment expert. 
    Help users identify skill gaps and create learning paths for STEM careers.
    Provide specific, actionable recommendations.""",
    
    "salary": """You are a compensation analyst for STEM careers.
    Provide realistic salary expectations and negotiation advice.
    Consider location, experience, and market trends."""
}