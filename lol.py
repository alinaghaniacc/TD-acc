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

    # Elegant Chanel-inspired header
    st.markdown("""
    <div class="header">
        <div class="header-title">Alina Ghani</div>
        <div class="header-subtitle">CONSULTANTE DATA</div>
    </div>
    """, unsafe_allow_html=True)

    # Tabs with elegant styling
    tabs = st.tabs(["Pullman", "Peugeot", "L'Oréal NOLI", "Chanel Foresight", "Sephora", "Extra Projects"])

    # Pullman Tab
    with tabs[0]:
        st.markdown("""
        <div class="project-banner">
            <div class="project-title">Pullman</div>
            <div class="project-date">Dec 2023 - Sept 2024</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Objective in frame
        st.markdown("""
        <div class="objective-container">
            <div class="objective-label">Objectif</div>
            <div class="objective-content">Générer du contenu pour 156 hôtels Pullman, chacun avec une identité de marque distincte</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Split container for Réalisations and Compétences
        st.markdown("""
        <div class="split-container">
            <div class="split-left">
                <div class="section-title">Réalisations</div>
                <ul class="bullet-list">
                    <li class="bullet-item">Création de "Molière", un outil de génération de texte utilisant +30 modèles d'IA</li>
                    <li class="bullet-item">Développement de l'infrastructure technique complète</li>
                    <li class="bullet-item">Définition des prompts en collaboration avec des copywriters</li>
                    <li class="bullet-item">Optimisation pour un anglais britannique authentique</li>
                    <li class="bullet-item">Création d'un site web pour recueillir les retours des 156 hôtels</li>
                </ul>
            </div>
            <div class="split-right">
                <div class="section-title">Compétences</div>
                <div class="competency-box">Prompt Engineering & Expertise IA</div>
                <div class="competency-box">Gestion de Projet & Méthodologies Accenture</div>
                <div class="competency-box">Autonomie sur les Livrables</div>
                <div class="competency-box">Relation Client & Satisfaction</div>
                <div class="competency-box">Veille Technologique & Innovation</div>
                <div class="competency-box">Travail en Équipe & Collaboration</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Feedbacks côte à côte
        col1, col2 = st.columns(2)

        # Feedback de Jennifer (à gauche)
        with col1:
            pullman_feedback_2 = load_image(feedback_images["pullman_2"])
            if pullman_feedback_2:
                st.markdown("""
                <div class="feedback-container">
                    <div class="feedback-label">Feedback</div>
                    <div class="feedback-content">
                """, unsafe_allow_html=True)
                st.image(pullman_feedback_2, caption="Feedback de Jennifer")
                st.markdown("</div></div>", unsafe_allow_html=True)

        # Feedback de Martial (à droite)
        with col2:
            pullman_feedback = load_image(feedback_images["pullman"])
            if pullman_feedback:
                st.markdown("""
                <div class="feedback-container">
                    <div class="feedback-label">Feedback</div>
                    <div class="feedback-content">
                """, unsafe_allow_html=True)
                st.image(pullman_feedback, caption="Feedback de Martial")
                st.markdown("</div></div>", unsafe_allow_html=True)

        # Interface Pullman en dessous
        pullman_ui = load_image(project_images["pullman_ui"])
        if pullman_ui:
            st.markdown("""
            <div class="feedback-container">
                <div class="feedback-label">Solution Développée</div>
                <div class="feedback-content">
            """, unsafe_allow_html=True)
            st.image(pullman_ui, caption="Interface Pullman Content Generation")
            st.markdown("</div></div>", unsafe_allow_html=True)

    # Peugeot Tab
    with tabs[1]:
        st.markdown("""
        <div class="project-banner">
            <div class="project-title">Peugeot</div>
            <div class="project-date">Sept 2024 - Nov 2024</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Objective in frame
        st.markdown("""
        <div class="objective-container">
            <div class="objective-label">Objectif</div>
            <div class="objective-content">Développement d'un chatbot pour le Salon de l'Automobile</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Split container for Réalisations and Compétences
        st.markdown("""
        <div class="split-container">
            <div class="split-left">
                <div class="section-title">Réalisations</div>
                <ul class="bullet-list">
                    <li class="bullet-item">Conception de l'IA sous-jacente</li>
                    <li class="bullet-item">Animation des workshops client pour définir les types de réponses attendues</li>
                    <li class="bullet-item">Création de la base de données de connaissances pour alimenter l'IA</li>
                    <li class="bullet-item">Mise en place de guardrails pour éviter les contenus problématiques</li>
                </ul>
            </div>
            <div class="split-right">
                <div class="section-title">Compétences</div>
                <div class="competency-box">Expertise Technique IA & Chatbots</div>
                <div class="competency-box">Animation d'Ateliers & Leadership</div>
                <div class="competency-box">Gestion des Risques & Guardrails</div>
                <div class="competency-box">Compréhension Écosystème Client</div>
                <div class="competency-box">Qualité des Livrables</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Images
        col1, col2 = st.columns(2)
        with col1:
            # Utiliser l'image du chatbot Peugeot
            peugeot_chatbot = load_image(project_images["peugeot_chatbot"])
            if peugeot_chatbot:
                st.markdown("""
                <div class="feedback-container">
                    <div class="feedback-label">Solution Développée</div>
                    <div class="feedback-content">
                """, unsafe_allow_html=True)
                st.image(peugeot_chatbot, caption="Interface chatbot Peugeot")
                st.markdown("</div></div>", unsafe_allow_html=True)
            else:
                st.image("https://via.placeholder.com/600x400", caption="Interface chatbot Peugeot")
        
        with col2:
            # Utiliser l'image de feedback de Jens avec style spécial
            peugeot_feedback = load_image(feedback_images["peugeot"])
            if peugeot_feedback:
                # Utiliser un conteneur similaire à celui de l'objectif
                st.markdown("""
                <div class="feedback-container">
                    <div class="feedback-label">Feedback</div>
                    <div class="feedback-content">
                """, unsafe_allow_html=True)
                st.image(peugeot_feedback, caption="Feedback de Jens")
                st.markdown("</div></div>", unsafe_allow_html=True)
            else:
                st.image("https://via.placeholder.com/600x400", caption="Salon de l'Auto")

    # L'Oréal NOLI Tab
    with tabs[2]:
        st.markdown("""
        <div class="project-banner">
            <div class="project-title">L'Oréal NOLI</div>
            <div class="project-date">Nov 2024</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Objective in frame
        st.markdown("""
        <div class="objective-container">
            <div class="objective-label">Objectif</div>
            <div class="objective-content">Automatisation par IA du processus de création visuelle pour les pages produits</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Split container for Réalisations and Compétences
        st.markdown("""
        <div class="split-container">
            <div class="split-left">
                <div class="section-title">Réalisations</div>
                <ul class="bullet-list">
                    <li class="bullet-item">Développement d'une application qui génère automatiquement des visuels produits</li>
                    <li class="bullet-item">Automatisation de la segmentation produit, génération de "smudge" (taches texturées)</li>
                    <li class="bullet-item">Sélection intelligente de l'arrière-plan parmi 6 couleurs prédéfinies</li>
                    <li class="bullet-item">Optimisation pour un temps de génération de 4 secondes par image</li>
                </ul>
            </div>
            <div class="split-right">
                <div class="section-title">Compétences</div>
                <div class="competency-box">Expertise Technique IA & Vision</div>
                <div class="competency-box">Autonomie sur Périmètre Technique</div>
                <div class="competency-box">Optimisation & Performance</div>
                <div class="competency-box">Gestion de Multiples Tâches</div>
                <div class="competency-box">Amélioration Continue</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Images
        col1, col2 = st.columns(2)
        with col1:
            # Utiliser l'image de l'application NOLI
            noli_app = load_image(project_images["noli_app"])
            if noli_app:
                st.markdown("""
                <div class="feedback-container">
                    <div class="feedback-label">Solution Développée</div>
                    <div class="feedback-content">
                """, unsafe_allow_html=True)
                st.image(noli_app, caption="Application NOLI")
                st.markdown("</div></div>", unsafe_allow_html=True)
            else:
                st.image("https://via.placeholder.com/600x400", caption="Application NOLI")
        
        with col2:
            # Utiliser l'image de feedback de Céline avec style spécial
            noli_feedback = load_image(feedback_images["noli"])
            if noli_feedback:
                # Utiliser un conteneur similaire à celui de l'objectif
                st.markdown("""
                <div class="feedback-container">
                    <div class="feedback-label">Feedback</div>
                    <div class="feedback-content">
                """, unsafe_allow_html=True)
                st.image(noli_feedback, caption="Feedback de Céline")
                st.markdown("</div></div>", unsafe_allow_html=True)
            else:
                st.image("https://via.placeholder.com/600x400", caption="Exemple de produit traité")

    # Chanel Foresight Tab
    with tabs[3]:
        st.markdown("""
        <div class="project-banner">
            <div class="project-title">Chanel Foresight</div>
            <div class="project-date">Nov 2024 - Fév 2025</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Objective in frame
        st.markdown("""
        <div class="objective-container">
            <div class="objective-label">Objectif</div>
            <div class="objective-content">Transformation d'un document stratégique de 300 pages en expérience interactive</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Split container for Réalisations and Compétences
        st.markdown("""
        <div class="split-container">
            <div class="split-left">
                <div class="section-title">Réalisations</div>
                <ul class="bullet-list">
                    <li class="bullet-item">Conversion du document en site web avec navigation intuitive</li>
                    <li class="bullet-item">Conception d'une mind map interactive pour faciliter l'exploration du contenu</li>
                    <li class="bullet-item">Implémentation d'un système RAG pour rechercher efficacement les contenus similaires</li>
                    <li class="bullet-item">Création d'une fonctionnalité de storytelling "Vision 2050" avec personnages fictifs</li>
                    <li class="bullet-item">Mise en place de filtres de génération et guardrails</li>
                </ul>
            </div>
            <div class="split-right">
                <div class="section-title">Compétences</div>
                <div class="competency-box">Expertise RAG & Systèmes IA</div>
                <div class="competency-box">Gestion de Projet Complexe</div>
                <div class="competency-box">Rédaction de RFP/Propositions</div>
                <div class="competency-box">Qualité & Innovation</div>
                <div class="competency-box">Méthodologies Accenture</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Feedback de Jason en premier
        chanel_feedback = load_image(feedback_images["chanel"])
        if chanel_feedback:
            st.markdown("""
            <div class="feedback-container">
                <div class="feedback-label">Feedback</div>
                <div class="feedback-content">
            """, unsafe_allow_html=True)
            st.image(chanel_feedback, caption="Feedback de Jason")
            st.markdown("</div></div>", unsafe_allow_html=True)

        # Mind map et Vision 2050 côte à côte
        col1, col2 = st.columns(2)
        with col1:
            chanel_mindmap = load_image(project_images["chanel_mindmap"])
            if chanel_mindmap:
                st.markdown("""
                <div class="feedback-container">
                    <div class="feedback-label">Solution Développée</div>
                    <div class="feedback-content">
                """, unsafe_allow_html=True)
                st.image(chanel_mindmap, caption="Mind map interactive")
                st.markdown("</div></div>", unsafe_allow_html=True)

        with col2:
            chanel_story = load_image(project_images["chanel_story"])
            if chanel_story:
                st.markdown("""
                <div class="feedback-container">
                    <div class="feedback-label">Solution Développée</div>
                    <div class="feedback-content">
                """, unsafe_allow_html=True)
                st.image(chanel_story, caption="Interface Vision 2050")
                st.markdown("</div></div>", unsafe_allow_html=True)

    # Sephora Tab
    with tabs[4]:
        st.markdown("""
        <div class="project-banner">
            <div class="project-title">Sephora</div>
            <div class="project-date">Mars 2025 - En cours</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Objective in frame with status
        st.markdown("""
        <div class="objective-container" style="position: relative;">
            <div class="objective-label">Objectif</div>
            <div class="objective-content">Création d'une plateforme de données pour toutes les marques Sephora</div>
            <div class="status">En cours</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Split container for Réalisations and Compétences
        st.markdown("""
        <div class="split-container">
            <div class="split-left">
                <div class="section-title">Réalisations</div>
                <ul class="bullet-list">
                    <li class="bullet-item">Définition des 100 KPIs critiques à calculer pour les différentes marques</li>
                    <li class="bullet-item">Analyse de faisabilité pour le calcul des KPIs avec les données disponibles</li>
                    <li class="bullet-item">Vérification de l'accessibilité des données</li>
                </ul>
            </div>
            <div class="split-right">
                <div class="section-title">Compétences</div>
                <div class="competency-box">Analyse de Données</div>
                <div class="competency-box">Définition de KPIs</div>
                <div class="competency-box">Architecture de Données</div>
                <div class="competency-box">Conseil Stratégique</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Images
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://via.placeholder.com/600x400", caption="Dashboard KPIs")
        with col2:
            st.image("https://via.placeholder.com/600x400", caption="Réunion de cadrage")

    # Extra Projects Tab
    with tabs[5]:
        # GenAI Breakfasts
        st.markdown("""
        <div class="project-banner">
            <div class="project-title">GenAI Breakfasts</div>
            <div class="project-date">2024 - 2025</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Objective in frame
        st.markdown("""
        <div class="objective-container">
            <div class="objective-label">Objectif</div>
            <div class="objective-content">Animation de sessions hebdomadaires sur l'IA générative pour former les équipes internes</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Split container for Réalisations and Compétences
        st.markdown("""
        <div class="split-container">
            <div class="split-left">
                <div class="section-title">Réalisations</div>
                <ul class="bullet-list">
                    <li class="bullet-item">Organisation de sessions hebdomadaires sur l'IA générative</li>
                    <li class="bullet-item">Animation d'ateliers de "battle de prompts" pour développer les compétences</li>
                    <li class="bullet-item">Formation aux bonnes pratiques de prompt engineering</li>
                    <li class="bullet-item">Sensibilisation aux deepfakes via démonstration d'un générateur</li>
                </ul>
            </div>
            <div class="split-right">
                <div class="section-title">Compétences</div>
                <div class="competency-box">Formation</div>
                <div class="competency-box">Animation d'Ateliers</div>
                <div class="competency-box">Pédagogie</div>
                <div class="competency-box">Veille Technologique</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Utiliser l'image de feedback de François avec style spécial
        genai_feedback = load_image(feedback_images["genai"])
        if genai_feedback:
            # Utiliser un conteneur similaire à celui de l'objectif
            st.markdown("""
            <div class="feedback-container">
                <div class="feedback-label">Feedback</div>
                <div class="feedback-content">
            """, unsafe_allow_html=True)
            st.image(genai_feedback, caption="Feedback de François")
            st.markdown("</div></div>", unsafe_allow_html=True)
        else:
            st.image("https://via.placeholder.com/800x400", caption="GenAI Breakfast")
        
        # External Interventions
        st.markdown("""
        <div class="project-banner">
            <div class="project-title">Interventions Externes</div>
            <div class="project-date">2025</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Objective in frame
        st.markdown("""
        <div class="objective-container">
            <div class="objective-label">Objectif</div>
            <div class="objective-content">Partage d'expertise sur l'IA générative auprès d'institutions académiques</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Split container for Réalisations and Compétences
        st.markdown("""
        <div class="split-container">
            <div class="split-left">
                <div class="section-title">Réalisations</div>
                <ul class="bullet-list">
                    <li class="bullet-item">Présentation à l'École des Mines Télécom au plateau de Saclay</li>
                    <li class="bullet-item">Conférence sur l'effet Mathilda et les initiatives d'Accenture</li>
                    <li class="bullet-item">Intervention devant plus de 100 étudiants</li>
                </ul>
            </div>
            <div class="split-right">
                <div class="section-title">Compétences</div>
                <div class="competency-box">Communication</div>
                <div class="competency-box">Prise de Parole en Public</div>
                <div class="competency-box">Vulgarisation Scientifique</div>
                <div class="competency-box">Représentation Institutionnelle</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Utiliser l'image de l'intervention à l'École des Mines
        mines_intervention = load_image(project_images["mines_intervention"])
        if mines_intervention:
            st.image(mines_intervention, caption="Intervention École des Mines")
        else:
            st.image("https://via.placeholder.com/800x400", caption="Intervention École des Mines")

    # Footer with Chanel-inspired design
    st.markdown("""
    <div class="footer">
        <div class="footer-title">Alina Ghani</div>
        <div class="footer-subtitle">CONSULTANTE DATA</div>
        <div class="footer-contact">alina.ghani@accenture.com | +33 6 36 12 27 62</div>
    </div>
    """, unsafe_allow_html=True)

# Entry point
if __name__ == "__main__":
    main()