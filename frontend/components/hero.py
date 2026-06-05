import streamlit as st
from pathlib import Path
import base64

def hero():
    image_path = Path("assets/image_1.jpg")
    try:
        with open(image_path, "rb") as img:
            encoded = base64.b64encode(img.read()).decode()
    except FileNotFoundError:
        encoded = ""

    st.markdown(f"""
    <style>
    @keyframes fadeInUp {{
        from {{ transform: translateY(20px); opacity: 0; }}
        to {{ transform: translateY(0); opacity: 1; }}
    }}
    
    .hero-banner {{
        height: 380px;
        border-radius: 24px;
        position: relative;
        overflow: hidden;
        background: 
            linear-gradient(rgba(7, 27, 77, 0.88), rgba(7, 27, 77, 0.92)),
            url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: center;
        padding: 60px;
        margin-bottom: 35px;
        box-shadow: 0 15px 35px rgba(7, 27, 77, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.08);
        animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}
    .hero-badge {{
        color: #D4A017;
        font-weight: 700;
        font-size: 11px;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        margin-bottom: 12px;
        background: rgba(212, 160, 23, 0.1);
        padding: 6px 12px;
        border-radius: 20px;
        display: inline-block;
        border: 1px solid rgba(212, 160, 23, 0.2);
    }}
    .hero-title {{
        color: white;
        font-size: 56px;
        font-weight: 800;
        line-height: 1.1;
        margin: 0;
        letter-spacing: -1px;
    }}
    .hero-subtitle {{
        color: #F1F5F9;
        font-size: 24px;
        font-weight: 400;
        margin-top: 8px;
        opacity: 0.95;
    }}
    .hero-description {{
        color: #CBD5E1;
        font-size: 15px;
        max-width: 700px;
        line-height: 1.6;
        margin-top: 18px;
    }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-banner">
        <div>
            <div class="hero-badge">Phase 1 Labs • Active Evaluation</div>
            <h1 class="hero-title">EchoDesk AI</h1>
            <div class="hero-subtitle">Sentiment-Aware Customer Support Assistant</div>
            <p class="hero-description">
                An advanced research platform designed to evaluate and map semantic response generations 
                across varying NLP engineering architectures and fine-tuning frameworks.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)