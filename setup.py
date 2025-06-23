from setuptools import setup, find_packages

setup(
    name="career-shift-stem",
    version="1.0.0",
    author="fabiyrizky",
    description="A Streamlit app for career transition to STEM fields",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.29.0",
        "pandas>=2.0.3",
        "numpy>=1.24.3",
        "plotly>=5.17.0",
        "scikit-learn>=1.3.0",
        "requests>=2.31.0",
        "Pillow>=10.0.0",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ]
    },
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "career-stem=app:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)