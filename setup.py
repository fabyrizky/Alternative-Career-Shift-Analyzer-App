"""
Setup script for downloading required data
"""
import nltk
import subprocess
import sys

def setup():
    """Download required NLTK data"""
    print("Downloading NLTK data...")
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')
    
    print("Downloading spaCy model...")
    try:
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    except:
        print("Could not download spaCy model. Will use fallback.")

if __name__ == "__main__":
    setup()
