import streamlit as st

def render_hero():
    st.markdown(
        """
        <style>
            .hero-box {
                background-image: linear-gradient(rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.85)), url('https://images.unsplash.com/photo-1451187580459-43490279c0fa');
                background-size: cover;
                background-position: center;
                border-radius: 12px;
                padding: 30px;
                border: 1px solid rgba(255, 255, 255, 0.08);
                transition: transform 0.25s ease;
                margin-bottom: 20px;
            }
            .hero-box:hover {
                transform: translateY(-2px);
            }
        </style>
        
        <div class="hero-box">
            <p style="font-size: 12px; color: #818cf8; font-weight: 700; margin: 0 0 6px 0; letter-spacing: 1px;">RESEARCH PROJECT CENTER</p>
            <h1 style="margin: 0 0 6px 0; font-size: 32px; font-weight: 800; color: #ffffff !important;">SupportAI Platform</h1>
            <h3 style="color: #e0e7ff !important; font-size: 18px; font-weight: 500; margin: 0 0 12px 0;">Smart Customer Support Automated Draft Engine</h3>
            <p style="font-size: 14.5px; line-height: 1.5; color: #cbd5e1 !important; margin: 0; max-width: 720px;">
                Built as an active research trial at IIT Indore. This system helps support staff review text trends, write answers instantly, and look up answers from data guides to help customers faster.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )