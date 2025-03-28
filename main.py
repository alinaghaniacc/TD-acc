import streamlit as st
from PIL import Image
import os
import io

def main():
    # Configuration de la page
    st.set_page_config(
        page_title="Alina Ghani | Portfolio",
        page_icon="✨",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Fonction pour charger les images locales
    def load_image(image_path):
        if os.path.exists(image_path):
            return Image.open(image_path)
        else:
            # Utiliser une image placeholder si l'image n'existe pas
            st.warning(f"Image non trouvée: {image_path}")
            return None
    
    # Chemins des images de feedback
    feedback_images = {
        "pullman": "images/martial_feedback.png",
        "pullman_2": "images/Feedback_Jennifer.png",
        "peugeot": "images/jens_feedback.png",
        "noli": "images/celine_feedback.png",
        "genai": "images/François_feedback.png",
        "chanel": "images/Feedback_Jason.png"
    }
    
    # Chemins des images de projet
    project_images = {
        "pullman_ui": "images/Pullman_ui.png",
        "peugeot_chatbot": "images/ev_chatbot.png",
        "noli_app": "images/Noli.png",
        "chanel_mindmap": "images/Chanel_fs_mindmap.png",
        "chanel_story": "images/chanel_fs_story.jpg",
        "mines_intervention": "images/Intervention_École_des_Mines.jpeg"
    }

    # Le reste de votre CSS reste inchangé avec ajout du style pour les feedbacks
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Montserrat:wght@300;400;500;600;700&display=swap');
        
        :root {
            --black: #000000;
            --white: #ffffff;
            --off-white: #f8f8f8;
            --accent-pink: #f2a0b5;
            --light-blue: #e6f0ff;
        }
        
        /* General styles */
        body {
            font-family: 'Montserrat', sans-serif;
            background-color: var(--white);
            color: var(--black);
            line-height: 1.6;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Cormorant Garamond', serif;
            font-weight: 500;
            letter-spacing: 0.02em;
        }
        
        h1 {
            font-size: 3rem;
            font-weight: 600;
        }
        
        h2 {
            font-size: 2.2rem;
            color: var(--black);
            margin-bottom: 1.5rem;
        }
        
        h3 {
            font-size: 1.5rem;
            color: var(--black);
            margin-top: 1.5rem;
            font-weight: 500;
        }
        
        p {
            font-weight: 300;
        }
        
        /* Header */
        .header {
            background-color: var(--black);
            padding: 3.5rem 2.5rem;
            color: var(--white);
            margin-bottom: 2.5rem;
            position: relative;
            text-align: center;
        }
        
        .header-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 3.5rem;
            font-weight: 500;
            letter-spacing: 0.1em;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
        }
        
        .header-subtitle {
            font-family: 'Montserrat', sans-serif;
            font-weight: 300;
            color: var(--white);
            font-size: 1.1rem;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }
        
        /* Project banner */
        .project-banner {
            background-color: var(--black);
            padding: 2rem;
            color: var(--white);
            margin-bottom: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border: 1px solid var(--black);
        }
        
        .project-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 2.5rem;
            font-weight: 500;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }
        
        .project-date {
            font-family: 'Montserrat', sans-serif;
            background-color: transparent;
            color: var(--accent-pink);
            font-size: 1rem;
            font-weight: 400;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }
        
        /* Objective box */
        .objective-container {
            border: 1px solid var(--black);
            margin-bottom: 2rem;
        }
        
        .objective-label {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.5rem;
            font-weight: 500;
            padding: 1rem;
            border-bottom: 1px solid var(--black);
        }
        
        .objective-content {
            background-color: var(--light-blue);
            padding: 1rem;
            font-family: 'Montserrat', sans-serif;
            font-weight: 400;
        }
        
        /* Feedback container */
        .feedback-container {
            border: 1px solid var(--black);
            margin-bottom: 2rem;
        }
        
        .feedback-label {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.5rem;
            font-weight: 500;
            padding: 1rem;
            border-bottom: 1px solid var(--black);
        }
        
        .feedback-content {
            padding: 0;
        }
        
        /* Split content */
        .split-container {
            display: flex;
            border: 1px solid var(--black);
            margin-bottom: 2rem;
        }
        
        .split-left {
            flex: 1;
            padding: 1.5rem;
            border-right: 1px solid var(--black);
        }
        
        .split-right {
            flex: 1;
            padding: 1.5rem;
        }
        
        .section-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.5rem;
            font-weight: 500;
            margin-bottom: 1.5rem;
            text-align: center;
        }
        
        /* Bullet points */
        .bullet-list {
            list-style-type: none;
            padding-left: 0;
        }
        
        .bullet-item {
            position: relative;
            padding-left: 1.5rem;
            margin-bottom: 1rem;
            font-family: 'Montserrat', sans-serif;
            font-weight: 300;
        }
        
        .bullet-item:before {
            content: "•";
            position: absolute;
            left: 0;
            color: var(--black);
            font-weight: bold;
        }
        
        /* Competency box */
        .competency-box {
            border: 1px solid var(--black);
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0;
            border-bottom: 1px solid var(--black);
            padding-bottom: 0;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: transparent;
            color: var(--black);
            font-family: 'Montserrat', sans-serif;
            font-weight: 400;
            font-size: 0.9rem;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            border: none;
            border-bottom: 3px solid transparent;
            border-radius: 0;
            margin-right: 2rem;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: transparent !important;
            color: var(--black) !important;
            font-weight: 500 !important;
            border-bottom: 3px solid var(--black) !important;
        }
        
        /* Image styling */
        .stImage > img {
            border: 1px solid var(--black);
        }
        
        /* Image captions */
        .stImage > div > div > p {
            font-family: 'Montserrat', sans-serif;
            color: var(--black);
            font-size: 0.8rem;
            font-weight: 400;
            text-align: center;
            margin-top: 0.5rem !important;
            font-style: italic;
        }
        
        /* Button styling */
        .stButton > button {
            background-color: var(--black) !important;
            color: var(--white) !important;
            font-family: 'Montserrat', sans-serif !important;
            font-size: 0.8rem !important;
            font-weight: 400 !important;
            letter-spacing: 0.05em !important;
            text-transform: uppercase !important;
            padding: 0.75rem 1.5rem !important;
            border: none !important;
            border-radius: 0 !important;
            transition: background-color 0.3s ease !important;
        }
        
        .stButton > button:hover {
            background-color: var(--accent-pink) !important;
        }
        
        /* Status indicator */
        .status {
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.75rem;
            font-family: 'Montserrat', sans-serif;
            font-size: 0.7rem;
            font-weight: 500;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            background-color: var(--accent-pink);
            color: var(--black);
            position: absolute;
            top: 1rem;
            right: 1rem;
        }
        
        /* Footer */
        .footer {
            background-color: var(--black);
            color: var(--white);
            padding: 2.5rem;
            text-align: center;
            font-family: 'Montserrat', sans-serif;
            font-weight: 300;
            margin-top: 2rem;
        }
        
        .footer-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.5rem;
            font-weight: 500;
            letter-spacing: 0.1em;
            margin-bottom: 1rem;
            text-transform: uppercase;
        }
        
        .footer-subtitle {
            font-size: 0.9rem;
            letter-spacing: 0.05em;
            margin-bottom: 1rem;
        }
        
        .footer-contact {
            font-size: 0.8rem;
            letter-spacing: 0.05em;
        }
        
        /* Hide default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .header {
                padding: 2rem 1rem;
            }
            
            .header-title {
                font-size: 2.5rem;
            }
            
            .split-container {
                flex-direction: column;
            }
            
            .split-left {
                border-right: none;
                border-bottom: 1px solid var(--black);
            }
        }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
    <div class="header">
        <div class="header-title">Alina Ghani</div>
        <div class="header-subtitle">AI & Tech Innovation Engineer</div>
    </div>
    """, unsafe_allow_html=True)

    # Tabs
    tabs = st.tabs(["ME", "Pullman", "Peugeot", "L'Oréal NOLI", "Chanel Foresight", "Sephora"])

    # ME Tab
    with tabs[0]:
        st.markdown("""
        <p style="color: #722F37; font-weight: bold; font-size: 1.2rem; text-align: center; margin-bottom: 2rem;">
            The best way to predict the future is to create it, and I'm talking about algorithms 😉
        </p>
        """, unsafe_allow_html=True)
        
        # Profile image
        profile_image = load_image("/Users/alina.ghani/Library/CloudStorage/OneDrive-Accenture/TD-accenture/images/mazarine.jpeg")
        if profile_image:
            st.image(profile_image)

    # Pullman Tab
    with tabs[1]:
        st.markdown("""
        <div class="project-banner">
            <div class="project-title">Pullman</div>
            <div class="project-date">Dec 2023 - Sept 2024</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="objective-container">
            <div class="objective-label">Objective</div>
            <div class="objective-content">Generate content for 156 Pullman hotels, each with a distinct brand identity</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="split-container">
            <div class="split-left">
                <div class="section-title">Achievements</div>
                <ul class="bullet-list">
                    <li class="bullet-item">Creation of "Molière", a text generation tool using +30 AI models</li>
                    <li class="bullet-item">Development of complete technical infrastructure</li>
                    <li class="bullet-item">Definition of prompts in collaboration with copywriters</li>
                    <li class="bullet-item">Optimization for authentic British English</li>
                    <li class="bullet-item">Creation of a website to collect feedback from 156 hotels</li>
                </ul>
            </div>
            <div class="split-right">
                <div class="section-title">Skills</div>
                <div class="competency-box">Prompt Engineering & AI Expertise</div>
                <div class="competency-box">Project Management & Accenture Methodologies</div>
                <div class="competency-box">Deliverable Autonomy</div>
                <div class="competency-box">Client Relations & Satisfaction</div>
                <div class="competency-box">Technology Watch & Innovation</div>
                <div class="competency-box">Teamwork & Collaboration</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Peugeot Tab
    with tabs[2]:
        st.markdown("""
        <div class="project-banner">
            <div class="project-title">Peugeot</div>
            <div class="project-date">Sept 2024 - Nov 2024</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="objective-container">
            <div class="objective-label">Objective</div>
            <div class="objective-content">Development of a chatbot for the Motor Show</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="split-container">
            <div class="split-left">
                <div class="section-title">Achievements</div>
                <ul class="bullet-list">
                    <li class="bullet-item">Design of the underlying AI</li>
                    <li class="bullet-item">Facilitation of client workshops to define expected response types</li>
                    <li class="bullet-item">Creation of knowledge database to feed the AI</li>
                    <li class="bullet-item">Implementation of guardrails to avoid problematic content</li>
                </ul>
            </div>
            <div class="split-right">
                <div class="section-title">Skills</div>
                <div class="competency-box">Technical AI & Chatbot Expertise</div>
                <div class="competency-box">Workshop Facilitation & Leadership</div>
                <div class="competency-box">Risk Management & Guardrails</div>
                <div class="competency-box">Client Ecosystem Understanding</div>
                <div class="competency-box">Deliverable Quality</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # L'Oréal NOLI Tab
    with tabs[3]:
        st.markdown("""
        <div class="project-banner">
            <div class="project-title">L'Oréal NOLI</div>
            <div class="project-date">Nov 2024</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="objective-container">
            <div class="objective-label">Objective</div>
            <div class="objective-content">AI automation of visual creation process for product pages</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="split-container">
            <div class="split-left">
                <div class="section-title">Achievements</div>
                <ul class="bullet-list">
                    <li class="bullet-item">Development of an application that automatically generates product visuals</li>
                    <li class="bullet-item">Automation of product segmentation, generation of textured smudges</li>
                    <li class="bullet-item">Intelligent background selection from 6 predefined colors</li>
                    <li class="bullet-item">Optimization for 4-second generation time per image</li>
                </ul>
            </div>
            <div class="split-right">
                <div class="section-title">Skills</div>
                <div class="competency-box">Technical AI & Vision Expertise</div>
                <div class="competency-box">Technical Scope Autonomy</div>
                <div class="competency-box">Optimization & Performance</div>
                <div class="competency-box">Multiple Task Management</div>
                <div class="competency-box">Continuous Improvement</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Chanel Foresight Tab
    with tabs[4]:
        st.markdown("""
        <div class="project-banner">
            <div class="project-title">Chanel Foresight</div>
            <div class="project-date">Nov 2024 - Feb 2025</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="objective-container">
            <div class="objective-label">Objective</div>
            <div class="objective-content">Transformation of a 300-page strategic document into an interactive experience</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="split-container">
            <div class="split-left">
                <div class="section-title">Achievements</div>
                <ul class="bullet-list">
                    <li class="bullet-item">Conversion of document into website with intuitive navigation</li>
                    <li class="bullet-item">Design of interactive mind map to facilitate content exploration</li>
                    <li class="bullet-item">Implementation of RAG system for efficient similar content search</li>
                    <li class="bullet-item">Creation of "Vision 2050" storytelling feature with fictional characters</li>
                    <li class="bullet-item">Implementation of generation filters and guardrails</li>
                </ul>
            </div>
            <div class="split-right">
                <div class="section-title">Skills</div>
                <div class="competency-box">RAG & AI Systems Expertise</div>
                <div class="competency-box">Complex Project Management</div>
                <div class="competency-box">RFP/Proposal Writing</div>
                <div class="competency-box">Quality & Innovation</div>
                <div class="competency-box">Accenture Methodologies</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Sephora Tab
    with tabs[5]:
        st.markdown("""
        <div class="project-banner">
            <div class="project-title">Sephora</div>
            <div class="project-date">March 2025 - Ongoing</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="objective-container" style="position: relative;">
            <div class="objective-label">Objective</div>
            <div class="objective-content">Creation of a data platform for all Sephora brands</div>
            <div class="status">Ongoing</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="split-container">
            <div class="split-left">
                <div class="section-title">Achievements</div>
                <ul class="bullet-list">
                    <li class="bullet-item">Definition of 100 critical KPIs to calculate for different brands</li>
                    <li class="bullet-item">Feasibility analysis for KPI calculation with available data</li>
                    <li class="bullet-item">Data accessibility verification</li>
                </ul>
            </div>
            <div class="split-right">
                <div class="section-title">Skills</div>
                <div class="competency-box">Data Analysis</div>
                <div class="competency-box">KPI Definition</div>
                <div class="competency-box">Data Architecture</div>
                <div class="competency-box">Strategic Consulting</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        <div class="footer-title">Alina Ghani</div>
        <div class="footer-subtitle">AI & Tech Innovation Engineer</div>
        <div class="footer-contact">alina.ghani@accenture.com | +33 6 36 12 27 62</div>
    </div>
    """, unsafe_allow_html=True)

# Entry point
if __name__ == "__main__":
    main()