"""
Skill Extractor Module
Extracts skills from user input text using NLP techniques
"""

import re
import pandas as pd
from typing import List, Dict, Set
import spacy
from collections import Counter
import os

class SkillExtractor:
    def __init__(self):
        """Initialize skill extractor with pre-defined skill database"""
        self.nlp = self._load_spacy_model()
        self.skill_database = self._load_skill_database()
        self.skill_synonyms = self._load_skill_synonyms()
        
    def _load_spacy_model(self):
        """Load spaCy model with error handling"""
        try:
            return spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading spaCy model...")
            os.system("python -m spacy download en_core_web_sm")
            return spacy.load("en_core_web_sm")
    
    def _load_skill_database(self) -> Set[str]:
        """Load comprehensive skill database"""
        # Core technical skills
        technical_skills = {
            # Programming Languages
            "python", "java", "javascript", "c++", "c#", "r", "sql", "html", "css",
            "typescript", "go", "rust", "swift", "kotlin", "scala", "php", "ruby",
            "matlab", "julia", "perl", "bash", "powershell", "vba", "sas", "stata",
            
            # Frameworks & Libraries
            "react", "angular", "vue", "django", "flask", "spring", "nodejs", "express",
            "tensorflow", "pytorch", "keras", "scikit-learn", "pandas", "numpy",
            "matplotlib", "seaborn", "plotly", "opencv", "nltk", "spacy",
            
            # Data & Analytics
            "data analysis", "data science", "machine learning", "deep learning",
            "statistical analysis", "data visualization", "big data", "data mining",
            "predictive modeling", "time series analysis", "a/b testing",
            
            # Cloud & DevOps
            "aws", "azure", "gcp", "docker", "kubernetes", "jenkins", "git",
            "ci/cd", "terraform", "ansible", "devops", "cloud computing",
            
            # Databases
            "mysql", "postgresql", "mongodb", "redis", "elasticsearch", "cassandra",
            "oracle", "sql server", "dynamodb", "neo4j", "firebase",
            
            # Industry Specific
            "blockchain", "smart contracts", "solidity", "web3", "ethereum",
            "cybersecurity", "penetration testing", "network security", "cryptography",
            "bioinformatics", "genomics", "iot", "robotics", "embedded systems",
            "cad", "autocad", "solidworks", "3d modeling", "simulation"
        }
        
        # Domain skills
        domain_skills = {
            "project management", "agile", "scrum", "product management",
            "business analysis", "financial analysis", "risk management",
            "marketing", "sales", "customer service", "supply chain",
            "quality assurance", "testing", "documentation", "technical writing"
        }
        
        # Soft skills
        soft_skills = {
            "communication", "leadership", "teamwork", "problem solving",
            "critical thinking", "creativity", "time management", "adaptability",
            "attention to detail", "analytical thinking", "presentation skills"
        }
        
        return technical_skills | domain_skills | soft_skills
    
    def _load_skill_synonyms(self) -> Dict[str, str]:
        """Load skill synonyms for better matching"""
        return {
            "ml": "machine learning",
            "dl": "deep learning",
            "ai": "artificial intelligence",
            "js": "javascript",
            "ts": "typescript",
            "k8s": "kubernetes",
            "algo": "algorithms",
            "stats": "statistics",
            "viz": "visualization",
            "db": "database",
            "dev": "development",
            "qa": "quality assurance"
        }
    
    def extract_skills(self, text: str) -> Dict[str, List[str]]:
        """
        Extract skills from input text
        
        Args:
            text: User input text containing skills and experience
            
        Returns:
            Dictionary with categorized skills
        """
        # Clean and preprocess text
        text = text.lower()
        text = self._expand_abbreviations(text)
        
        # Extract using multiple methods
        pattern_skills = self._extract_by_patterns(text)
        nlp_skills = self._extract_by_nlp(text)
        keyword_skills = self._extract_by_keywords(text)
        
        # Combine all extracted skills
        all_skills = pattern_skills | nlp_skills | keyword_skills
        
        # Categorize skills
        categorized_skills = self._categorize_skills(all_skills)
        
        return categorized_skills
    
    def _expand_abbreviations(self, text: str) -> str:
        """Expand common abbreviations"""
        for abbr, full in self.skill_synonyms.items():
            text = re.sub(r'\b' + abbr + r'\b', full, text)
        return text
    
    def _extract_by_patterns(self, text: str) -> Set[str]:
        """Extract skills using regex patterns"""
        skills = set()
        
        # Pattern for skills with years of experience
        exp_pattern = r'(\w+(?:\s+\w+)*)\s*[-–]\s*(\d+)\s*(?:years?|yrs?)'
        matches = re.findall(exp_pattern, text)
        for skill, _ in matches:
            if skill.lower() in self.skill_database:
                skills.add(skill.lower())
        
        # Pattern for listed skills
        list_pattern = r'(?:skills?|technologies|tools?):\s*(.*?)(?:\.|$)'
        matches = re.findall(list_pattern, text, re.IGNORECASE)
        for match in matches:
            skill_list = [s.strip() for s in re.split(r'[,;]', match)]
            for skill in skill_list:
                if skill.lower() in self.skill_database:
                    skills.add(skill.lower())
        
        return skills
    
    def _extract_by_nlp(self, text: str) -> Set[str]:
        """Extract skills using NLP techniques"""
        skills = set()
        doc = self.nlp(text)
        
        # Extract noun phrases
        for chunk in doc.noun_chunks:
            chunk_text = chunk.text.lower()
            if chunk_text in self.skill_database:
                skills.add(chunk_text)
        
        # Extract entities
        for ent in doc.ents:
            if ent.label_ in ["ORG", "PRODUCT", "LANGUAGE"]:
                ent_text = ent.text.lower()
                if ent_text in self.skill_database:
                    skills.add(ent_text)
        
        return skills
    
    def _extract_by_keywords(self, text: str) -> Set[str]:
        """Extract skills by keyword matching"""
        skills = set()
        words = text.lower().split()
        
        # Single word skills
        for word in words:
            if word in self.skill_database:
                skills.add(word)
        
        # Multi-word skills
        for i in range(len(words) - 1):
            bigram = f"{words[i]} {words[i+1]}"
            if bigram in self.skill_database:
                skills.add(bigram)
            
            if i < len(words) - 2:
                trigram = f"{words[i]} {words[i+1]} {words[i+2]}"
                if trigram in self.skill_database:
                    skills.add(trigram)
        
        return skills
    
    def _categorize_skills(self, skills: Set[str]) -> Dict[str, List[str]]:
        """Categorize skills into technical, domain, and soft skills"""
        categorized = {
            "technical": [],
            "domain": [],
            "soft": [],
            "tools": []
        }
        
        # Define category keywords
        technical_keywords = {"programming", "coding", "development", "engineering",
                            "analysis", "science", "learning", "algorithm"}
        domain_keywords = {"management", "business", "finance", "marketing", "sales"}
        soft_keywords = {"communication", "leadership", "teamwork", "problem", "thinking"}
        tool_keywords = {"aws", "docker", "git", "jenkins", "excel", "tableau"}
        
        for skill in skills:
            skill_lower = skill.lower()
            
            # Check for exact matches first
            if any(keyword in skill_lower for keyword in tool_keywords):
                categorized["tools"].append(skill)
            elif any(keyword in skill_lower for keyword in technical_keywords):
                categorized["technical"].append(skill)
            elif any(keyword in skill_lower for keyword in domain_keywords):
                categorized["domain"].append(skill)
            elif any(keyword in skill_lower for keyword in soft_keywords):
                categorized["soft"].append(skill)
            else:
                # Default to technical if unsure
                categorized["technical"].append(skill)
        
        # Remove duplicates and sort
        for category in categorized:
            categorized[category] = sorted(list(set(categorized[category])))
        
        return categorized
    
    def get_skill_relevance_scores(self, skills: List[str], industry: str) -> Dict[str, float]:
        """
        Calculate relevance scores for skills in a specific industry
        
        Args:
            skills: List of skills
            industry: Target industry
            
        Returns:
            Dictionary of skill: relevance_score
        """
        # This would ideally use a trained model or industry-specific data
        # For now, using a simple heuristic
        from config import FUTURE_INDUSTRIES
        
        industry_skills = set()
        if industry in FUTURE_INDUSTRIES:
            industry_skills = set(FUTURE_INDUSTRIES[industry]["key_skills"])
            industry_skills = {s.lower() for s in industry_skills}
        
        scores = {}
        for skill in skills:
            skill_lower = skill.lower()
            if skill_lower in industry_skills:
                scores[skill] = 1.0
            elif any(ind_skill in skill_lower for ind_skill in industry_skills):
                scores[skill] = 0.8
            else:
                scores[skill] = 0.3
        
        return scores
