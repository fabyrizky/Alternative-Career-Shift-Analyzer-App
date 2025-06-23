"""
Career Shift to Future STEM Industry - Main Streamlit App
"""

import streamlit as st
import pandas as pd
from typing import Dict, List
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Setup NLTK data on first run
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')

# Import custom modules
from config import APP_NAME, APP_DESCRIPTION, FUTURE_INDUSTRIES
from utils.skill_extractor import SkillExtractor
from utils.career_mapper import CareerMapper
from utils.readiness_score import ReadinessCalculator
from components.ui_components import *
from components.visualizations import *

# Page configuration
st.set_page_config(
    page_title=APP_NAME,
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = {}

# Initialize components
@st.cache_resource
def init_components():
    """Initialize all components"""
    return {
        'skill_extractor': SkillExtractor(),
        'career_mapper': CareerMapper(),
        'readiness_calculator': ReadinessCalculator()
    }

components = init_components()

# Sidebar navigation
def render_sidebar():
    """Render sidebar navigation"""
    with st.sidebar:
        st.markdown("## 🧭 Navigation")
        
        if st.button("🏠 Home", use_container_width=True):
            st.session_state.current_page = 'home'
            
        if st.button("📊 Career Analysis", use_container_width=True):
            st.session_state.current_page = 'analysis'
            
        if st.button("🎯 Industry Explorer", use_container_width=True):
            st.session_state.current_page = 'explorer'
            
        if st.button("📚 Learning Resources", use_container_width=True):
            st.session_state.current_page = 'resources'
            
        if st.button("📈 Market Insights", use_container_width=True):
            st.session_state.current_page = 'insights'
            
        st.markdown("---")
        st.markdown("### 💡 Quick Tips")
        st.info(
            "1. Be honest about your current skills\n"
            "2. Consider multiple industries\n"
            "3. Focus on transferable skills\n"
            "4. Set realistic timelines"
        )
        
        st.markdown("---")
        st.markdown("### 📞 Need Help?")
        st.markdown("[Documentation](https://github.com/)")
        st.markdown("[Report an Issue](https://github.com/)")

# Main pages
def home_page():
    """Home page"""
    render_header()
    
    # Introduction section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Welcome to Your Career Transformation Journey! 
        
        This AI-powered tool helps you:
        - 🔍 **Analyze** your current skills and experience
        - 🎯 **Identify** the best future STEM industries for you
        - 📊 **Measure** your readiness for career transition
        - 🗺️ **Map** personalized learning paths
        - 💼 **Discover** new career opportunities
        
        **Ready to explore your future in STEM?** Let's get started!
        """)
        
        if st.button("🚀 Start Career Analysis", type="primary", use_container_width=True):
            st.session_state.current_page = 'analysis'
            st.rerun()
            
    with col2:
        st.image("https://via.placeholder.com/400x300/1E88E5/FFFFFF?text=Future+STEM+Careers", 
                caption="Transform your career", use_column_width=True)
    
    # Feature cards
    st.markdown("### 🌟 Featured Industries")
    cols = st.columns(4)
    
    for i, (key, info) in enumerate(list(FUTURE_INDUSTRIES.items())[:4]):
        with cols[i]:
            st.markdown(f"""
            <div style="text-align: center; padding: 20px; background-color: #f0f0f0; 
                        border-radius: 10px; height: 150px;">
                <h1>{info['icon']}</h1>
                <h4>{info['name']}</h4>
            </div>
            """, unsafe_allow_html=True)
    
    # Statistics section
    st.markdown("### 📊 Industry Growth Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("AI/ML Jobs Growth", "74%", "5-year projection")
    with col2:
        st.metric("Avg. Salary Increase", "45%", "After transition")
    with col3:
        st.metric("Success Rate", "82%", "With proper preparation")
    with col4:
        st.metric("Time to Transition", "9-12", "Months average")

def analysis_page():
    """Career analysis page"""
    st.title("📊 Career Transition Analysis")
    st.markdown("Let's analyze your background and find the best STEM career path for you.")
    
    # Progress indicator
    progress = st.progress(0)
    
    # Step 1: User Input
    with st.container():
        st.header("Step 1: Your Background")
        user_inputs = render_skill_input_section()
        
        # Validate inputs
        if st.button("Analyze My Profile", type="primary"):
            if not user_inputs['current_role'] or not user_inputs['skills_text']:
                st.error("Please fill in at least your current role and skills!")
                return
            
            progress.progress(33)
            
            # Process skills
            with st.spinner("Extracting and analyzing your skills..."):
                extracted_skills = components['skill_extractor'].extract_skills(
                    user_inputs['skills_text']
                )
                st.session_state.user_data = {
                    **user_inputs,
                    'skills': extracted_skills
                }
            
            st.success(f"✅ Found {sum(len(v) for v in extracted_skills.values())} skills!")
            
            # Display extracted skills
            st.subheader("Extracted Skills")
            cols = st.columns(len(extracted_skills))
            for i, (category, skills) in enumerate(extracted_skills.items()):
                with cols[i]:
                    st.markdown(f"**{category.title()} Skills**")
                    for skill in skills:
                        st.write(f"• {skill}")
    
    # Step 2: Industry Selection
    if st.session_state.user_data:
        progress.progress(66)
        st.header("Step 2: Select Target Industry")
        
        selected_industry = render_industry_selector()
        
        if selected_industry:
            st.session_state.user_data['target_industry'] = selected_industry
            
            # Step 3: Analysis Results
            progress.progress(100)
            with st.spinner("Analyzing career transition feasibility..."):
                # Career mapping
                transition_analysis = components['career_mapper'].map_career_transition(
                    st.session_state.user_data['current_role'],
                    selected_industry
                )
                
                # Readiness calculation
                readiness_analysis = components['readiness_calculator'].calculate_readiness_score(
                    st.session_state.user_data,
                    selected_industry
                )
                
                st.session_state.analysis_results = {
                    'transition': transition_analysis,
                    'readiness': readiness_analysis
                }
            
            # Display results
            st.header("📋 Analysis Results")
            
            # Overall readiness
            col1, col2 = st.columns([1, 2])
            with col1:
                fig = render_readiness_gauge(
                    readiness_analysis['overall_score'],
                    "Overall Readiness"
                )
                st.plotly_chart(fig, use_container_width=True)
                
                st.metric("Readiness Level", readiness_analysis['readiness_level'])
                st.metric("Time to Ready", readiness_analysis['time_to_ready'])
                
            with col2:
                # Component scores
                st.subheader("Detailed Scores")
                for component, score in readiness_analysis['component_scores'].items():
                    render_progress_bar(
                        component.replace('_', ' ').title(),
                        score,
                        get_score_color(score)
                    )
            
            # Transition details
            st.subheader("🔄 Career Transition Path")
            transition_tab1, transition_tab2, transition_tab3 = st.tabs(
                ["Timeline", "Skills Gap", "Recommendations"]
            )
            
            with transition_tab1:
                render_career_path_timeline(transition_analysis['career_path'])
                
            with transition_tab2:
                # Skills gap analysis
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**✅ Your Transferable Skills**")
                    for skill in transition_analysis['transferable_skills'][:5]:
                        st.write(f"• {skill}")
                        
                with col2:
                    st.markdown("**📚 Skills to Develop**")
                    for skill in transition_analysis['skill_gaps'][:5]:
                        st.write(f"• {skill}")
                
                # Visualization
                current_skills = []
                for skills in st.session_state.user_data['skills'].values():
                    current_skills.extend(skills)
                    
                required_skills = FUTURE_INDUSTRIES[selected_industry]['key_skills']
                fig = render_skill_gap_chart(current_skills, required_skills)
                st.plotly_chart(fig, use_container_width=True)
                
            with transition_tab3:
                render_recommendations(readiness_analysis['recommendations'])
                
                # Next steps
                st.subheader("🎯 Your Next Steps")
                for i, step in enumerate(readiness_analysis['next_steps'], 1):
                    st.write(f"{i}. {step}")
            
            # Save results button
            if st.button("💾 Save Analysis Report"):
                # Generate report
                report = generate_analysis_report(
                    st.session_state.user_data,
                    st.session_state.analysis_results
                )
                st.download_button(
                    "📥 Download Report",
                    report,
                    "career_analysis_report.txt",
                    "text/plain"
                )

def explorer_page():
    """Industry explorer page"""
    st.title("🎯 Industry Explorer")
    st.markdown("Explore different future STEM industries and their requirements.")
    
    # Industry filter
    search_term = st.text_input("🔍 Search industries", placeholder="e.g., AI, Blockchain, Space")
    
    # Display industry cards
    for key, info in FUTURE_INDUSTRIES.items():
        if search_term.lower() in info['name'].lower() or not search_term:
            with st.expander(f"{info['icon']} {info['name']}", expanded=False):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**Description:** {info['description']}")
                    st.markdown("**Key Skills Required:**")
                    
                    # Skills grid
                    skills_cols = st.columns(3)
                    for i, skill in enumerate(info['key_skills']):
                        with skills_cols[i % 3]:
                            st.write(f"• {skill}")
                    
                    # Career roles
                    potential_roles = components['career_mapper']._get_potential_roles(key)
                    st.markdown("**Potential Roles:**")
                    roles_cols = st.columns(2)
                    for i, role in enumerate(potential_roles[:6]):
                        with roles_cols[i % 2]:
                            st.write(f"• {role}")
                
                with col2:
                    # Industry metrics
                    st.metric("Market Demand", "High", "↑ 15%")
                    st.metric("Avg. Salary", "$95,000", "↑ 8%")
                    st.metric("Job Growth", "22%", "5-year projection")
                    
                    if st.button(f"Analyze for {info['name']}", key=f"analyze_{key}"):
                        st.session_state.user_data['target_industry'] = key
                        st.session_state.current_page = 'analysis'
                        st.rerun()

def resources_page():
    """Learning resources page"""
    st.title("📚 Learning Resources")
    st.markdown("Find the best courses and resources for your career transition.")
    
    # Load course data
    try:
        courses_df = pd.read_csv(os.path.join("data", "course_catalog.csv"))
    except:
        st.error("Course catalog not found. Using sample data.")
        courses_df = pd.DataFrame({
            'course_name': ['Python Basics', 'Machine Learning'],
            'platform': ['Coursera', 'Udemy'],
            'industry': ['AI', 'AI'],
            'duration_weeks': [4, 8],
            'price_usd': [0, 49.99],
            'rating': [4.8, 4.7]
        })
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        industry_filter = st.selectbox(
            "Industry",
            ["All"] + list(FUTURE_INDUSTRIES.keys())
        )
    
    with col2:
        platform_filter = st.selectbox(
            "Platform",
            ["All"] + list(courses_df['platform'].unique())
        )
    
    with col3:
        price_filter = st.select_slider(
            "Max Price",
            options=[0, 20, 50, 100, 200, 500],
            value=100
        )
    
    # Filter courses
    filtered_courses = courses_df
    if industry_filter != "All":
        filtered_courses = filtered_courses[filtered_courses['industry'] == industry_filter]
    if platform_filter != "All":
        filtered_courses = filtered_courses[filtered_courses['platform'] == platform_filter]
    filtered_courses = filtered_courses[filtered_courses['price_usd'] <= price_filter]
    
    # Display courses
    st.subheader(f"Found {len(filtered_courses)} courses")
    
    for _, course in filtered_courses.iterrows():
        with st.container():
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            
            with col1:
                st.markdown(f"**{course['course_name']}**")
                st.caption(f"{course['platform']} | {course['industry']}")
                
            with col2:
                st.metric("Duration", f"{course['duration_weeks']} weeks")
                
            with col3:
                price_text = "Free" if course['price_usd'] == 0 else f"${course['price_usd']}"
                st.metric("Price", price_text)
                
            with col4:
                st.metric("Rating", f"⭐ {course['rating']}")
                
            st.markdown("---")

def insights_page():
    """Market insights page"""
    st.title("📈 Market Insights")
    st.markdown("Stay updated with the latest trends in future STEM industries.")
    
    # Industry comparison
    st.subheader("Industry Comparison")
    fig = create_industry_demand_chart()
    st.plotly_chart(fig, use_container_width=True)
    
    # Salary projections
    st.subheader("Salary Projections")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        current_salary = st.number_input(
            "Your Current Salary ($)",
            min_value=30000,
            max_value=500000,
            value=70000,
            step=5000
        )
        
        target_industry = st.selectbox(
            "Target Industry",
            list(FUTURE_INDUSTRIES.keys())
        )
    
    with col2:
        fig = create_salary_projection(current_salary, target_industry)
        st.plotly_chart(fig, use_container_width=True)
    
    # Industry news and trends
    st.subheader("🔥 Hot Skills in Demand")
    
    hot_skills = {
        "AI": ["GPT/LLM Development", "Computer Vision", "MLOps", "AI Ethics"],
        "BLOCKCHAIN": ["DeFi Development", "NFT Platforms", "Layer 2 Solutions", "Cross-chain Bridges"],
        "CYBERSECURITY": ["Cloud Security", "Zero Trust Architecture", "AI Security", "IoT Security"],
        "RENEWABLE": ["Grid Storage", "Hydrogen Tech", "Smart Grid AI", "Carbon Capture"]
    }
    
    cols = st.columns(2)
    for i, (industry, skills) in enumerate(list(hot_skills.items())[:4]):
        with cols[i % 2]:
            st.markdown(f"**{FUTURE_INDUSTRIES[industry]['icon']} {industry}**")
            for skill in skills:
                st.write(f"• {skill}")

def generate_analysis_report(user_data: Dict, results: Dict) -> str:
    """Generate text report of analysis"""
    report = f"""
CAREER TRANSITION ANALYSIS REPORT
================================

Date: {pd.Timestamp.now().strftime('%Y-%m-%d')}

PERSONAL PROFILE
---------------
Current Role: {user_data.get('current_role', 'N/A')}
Experience: {user_data.get('experience_years', 0)} years
Education: {user_data.get('education_level', 'N/A')}
Target Industry: {FUTURE_INDUSTRIES[user_data['target_industry']]['name']}

READINESS ASSESSMENT
-------------------
Overall Score: {results['readiness']['overall_score']}%
Readiness Level: {results['readiness']['readiness_level']}
Estimated Time to Ready: {results['readiness']['time_to_ready']}

SKILLS ANALYSIS
--------------
Transferable Skills: {', '.join(results['transition']['transferable_skills'][:5])}
Skills to Develop: {', '.join(results['transition']['skill_gaps'][:5])}

RECOMMENDATIONS
--------------
"""
    
    for i, rec in enumerate(results['readiness']['recommendations'], 1):
        report += f"{i}. {rec}\n"
    
    report += "\nNEXT STEPS\n----------\n"
    for i, step in enumerate(results['readiness']['next_steps'], 1):
        report += f"{i}. {step}\n"
    
    return report

# Main app logic
def main():
    """Main application entry point"""
    render_sidebar()
    
    # Route to appropriate page
    if st.session_state.current_page == 'home':
        home_page()
    elif st.session_state.current_page == 'analysis':
        analysis_page()
    elif st.session_state.current_page == 'explorer':
        explorer_page()
    elif st.session_state.current_page == 'resources':
        resources_page()
    elif st.session_state.current_page == 'insights':
        insights_page()
    
    # Footer
    render_footer()

if __name__ == "__main__":
    main()
