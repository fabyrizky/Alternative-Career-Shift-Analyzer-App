"""
Configuration settings for Career Shift Analyzer
"""

# App Settings
APP_NAME = "Career Shift to Future STEM Industry 🚀"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "AI-powered career transition analyzer for future STEM industries"

# Industries Configuration
FUTURE_INDUSTRIES = {
    "AI": {
        "name": "AI & Machine Learning",
        "icon": "🤖",
        "description": "Artificial Intelligence, Machine Learning, Deep Learning",
        "key_skills": ["Python", "TensorFlow", "PyTorch", "Machine Learning", "Deep Learning", 
                       "NLP", "Computer Vision", "Data Science", "Statistics"]
    },
    "BLOCKCHAIN": {
        "name": "Blockchain & Web3",
        "icon": "⛓️",
        "description": "Blockchain Development, Smart Contracts, DeFi",
        "key_skills": ["Solidity", "Web3.js", "Smart Contracts", "Ethereum", "DeFi", 
                       "Cryptography", "JavaScript", "Node.js", "Rust"]
    },
    "CYBERSECURITY": {
        "name": "Cybersecurity",
        "icon": "🔒",
        "description": "Information Security, Ethical Hacking, Security Architecture",
        "key_skills": ["Network Security", "Penetration Testing", "SIEM", "Cryptography",
                       "Security Auditing", "Python", "Linux", "Cloud Security", "DevSecOps"]
    },
    "BIOTECH": {
        "name": "BioTech & HealthTech",
        "icon": "🧬",
        "description": "Biotechnology, Medical Technology, Bioinformatics",
        "key_skills": ["Bioinformatics", "Genomics", "Python", "R", "Machine Learning",
                       "Molecular Biology", "Data Analysis", "Clinical Research", "Biostatistics"]
    },
    "AGRITECH": {
        "name": "Agriculture & FoodTech",
        "icon": "🌾",
        "description": "Smart Farming, Precision Agriculture, Food Innovation",
        "key_skills": ["IoT", "Data Analytics", "GIS", "Remote Sensing", "Python",
                       "Agricultural Science", "Sustainability", "Supply Chain", "Automation"]
    },
    "AQUATECH": {
        "name": "Aquaculture & Marine Tech",
        "icon": "🐟",
        "description": "Sustainable Aquaculture, Marine Biotechnology, Ocean Tech",
        "key_skills": ["Marine Biology", "Water Quality Analysis", "IoT", "Data Analytics",
                       "Sustainability", "Automation", "Environmental Science", "Python"]
    },
    "SPACETECH": {
        "name": "SpaceTech & Exploration",
        "icon": "🚀",
        "description": "Space Technology, Satellite Systems, Space Exploration",
        "key_skills": ["Aerospace Engineering", "Python", "MATLAB", "Orbital Mechanics",
                       "Satellite Systems", "Robotics", "Systems Engineering", "C++", "Simulation"]
    },
    "RENEWABLE": {
        "name": "New & Renewable Energy",
        "icon": "♻️",
        "description": "Solar, Wind, Battery Tech, Energy Storage, Smart Grid",
        "key_skills": ["Energy Systems", "Python", "MATLAB", "Power Electronics",
                       "Grid Integration", "Battery Technology", "Solar/Wind Energy", 
                       "Energy Storage", "Sustainability"]
    }
}

# Skill Categories
SKILL_CATEGORIES = {
    "technical": ["Programming", "Software Development", "Data Analysis", "Engineering"],
    "domain": ["Industry Knowledge", "Domain Expertise", "Specialized Skills"],
    "soft": ["Communication", "Leadership", "Problem Solving", "Teamwork"],
    "tools": ["Software Tools", "Platforms", "Frameworks", "Technologies"]
}

# Learning Platform URLs
LEARNING_PLATFORMS = {
    "coursera": "https://www.coursera.org/search?query=",
    "udemy": "https://www.udemy.com/courses/search/?q=",
    "edx": "https://www.edx.org/search?q=",
    "udacity": "https://www.udacity.com/courses/all?search=",
    "pluralsight": "https://www.pluralsight.com/search?q=",
    "linkedin": "https://www.linkedin.com/learning/search?keywords="
}

# Scoring Weights
SCORING_WEIGHTS = {
    "current_skills_match": 0.35,
    "transferable_skills": 0.25,
    "learning_curve": 0.20,
    "market_demand": 0.20
}

# UI Configuration
UI_CONFIG = {
    "primary_color": "#1E88E5",
    "secondary_color": "#FFC107",
    "success_color": "#4CAF50",
    "warning_color": "#FF9800",
    "danger_color": "#F44336",
    "page_icon": "🚀",
    "layout": "wide"
}

# Cache Settings
CACHE_TTL = 3600  # 1 hour in seconds

# File Paths
DATA_DIR = "data"
MODELS_DIR = "models"
CACHE_DIR = ".cache"
