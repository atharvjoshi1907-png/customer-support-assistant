import streamlit as st
import base64
import os
from views.research import render_research_view
from views.assistant import render_assistant_view
from views.analytics import render_analytics_view
from views.comparisons import render_comparison_view
from views.contact import render_contact_view

# Configure the page framework with your custom logo as the browser favicon
logo_path = os.path.join("assets", "logo.png")
if os.path.exists(logo_path):
    st.set_page_config(page_title="Sentix AI Platform", page_icon=logo_path, layout="wide", initial_sidebar_state="collapsed")
else:
    st.set_page_config(page_title="Sentix AI Platform", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# Safe asset helper for the background watermark logo
def get_base64_logo():
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

logo_base64 = get_base64_logo()
logo_watermark_style = ""
if logo_base64:
    logo_watermark_style = f"""
    .stApp::before {{
        content: "";
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 160px;
        height: 140px;
        background-image: url("data:image/png;base64,{logo_base64}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        opacity: 0.02;
        pointer-events: none;
        z-index: 1;
    }}
    """

# Senior-Friendly High Contrast Accessibility UI Layer Styling
st.markdown(f"""
<style>
    /* Global Canvas Reset & Interactive Matrix Background Blueprint */
    .stApp, .main, .block-container, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {{
        background-color: #0b0f19 !important;
        background-image: 
            linear-gradient(rgba(56, 189, 248, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(56, 189, 248, 0.03) 1px, transparent 1px),
            radial-gradient(circle at 50% 0%, #1e1b4b 0%, #0f172a 70%, #070a13 100%) !important;
        background-size: 40px 40px, 40px 40px, 100% 100% !important;
        background-attachment: fixed !important;
        color: #ffffff !important;
        font-family: system-ui, -apple-system, sans-serif !important;
    }}
    
    /* Optimized padding allocation for visibility scanning */
    .block-container {{
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
    }}
    
    {logo_watermark_style}

    /* Core Page Entry Shift Animation Blueprint */
    @keyframes stitchFadeEntrance {{
        0% {{ opacity: 0; transform: translateY(12px); filter: blur(3px); }}
        100% {{ opacity: 1; transform: translateY(0); filter: blur(0); }}
    }}
    
    [data-testid="stVerticalBlock"] > div {{
        animation: stitchFadeEntrance 0.45s cubic-bezier(0.16, 1, 0.3, 1) both;
    }}

    /* Global Containment Fix */
    div[data-testid="stVerticalBlock"], 
    div[data-testid="element-container"], 
    .element-container,
    div[data-class="stMarkdownContainer"] {{
        background-color: transparent !important;
    }}

    /* High-Visibility Brand Title */
    .saas-header-inline {{
        padding: 0 0 14px 0;
        margin-bottom: 25px;
        border-bottom: 2px solid rgba(56, 189, 248, 0.25);
    }}

    .nav-brand-text {{
        font-size: 32px;
        font-weight: 900;
        color: #38bdf8;
        letter-spacing: -0.5px;
    }}

    /* Navigation Container Map */
    div[data-testid="stHorizontalBlock"] {{
        background: transparent !important;
        padding: 0 !important;
        align-items: center !important;
        margin-bottom: 35px !important;
    }}

    /* ACCESSIBILITY: Large Frame Font Links for Senior Eye-Tracking Scales */
    div.stButton > button {{
        background-color: rgba(255, 255, 255, 0.03) !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        font-size: 19px !important;
        font-weight: 700 !important;
        transition: all 0.2s ease-in-out !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        cursor: pointer !important;
        text-align: center !important;
    }}
    
    /* High contrast hover actions */
    div.stButton > button:first-child:hover,
    div.stButton > button:hover {{
        background-color: #38bdf8 !important;
        color: #070a13 !important;
        border-color: #38bdf8 !important;
        transform: translateY(-2px) !important;
    }}
    
    div.stButton > button:hover p,
    div.stButton > button:hover span,
    div.stButton > button:hover div {{
        color: #070a13 !important;
    }}
    
    /* High Contrast Active Navigation State */
    div.stButton > button[data-testid="baseButton-primary"] {{
        background-color: rgba(56, 189, 248, 0.2) !important;
        color: #38bdf8 !important;
        font-weight: 800 !important;
        border: 2px solid #38bdf8 !important;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.25) !important;
    }}
    
    div.stButton > button[data-testid="baseButton-primary"] p {{
        color: #38bdf8 !important;
    }}

    /* ACCESSIBILITY: Force Globally Sharp Typography Weights & Scaled Heights */
    p, span, label, [data-testid="stWidgetLabel"] {{
        color: #f1f5f9 !important;
        font-size: 18.5px !important;
        line-height: 1.75 !important;
        font-weight: 500 !important;
    }}
    
    h1 {{ font-size: 42px !important; font-weight: 800 !important; color: #ffffff !important; }}
    h2 {{ font-size: 32px !important; font-weight: 800 !important; color: #ffffff !important; margin-top: 20px !important; }}
    h3 {{ font-size: 26px !important; font-weight: 700 !important; color: #ffffff !important; }}
    h4 {{ font-size: 22px !important; font-weight: 700 !important; color: #38bdf8 !important; }}
    
    /* Input Form Font Size Scaling */
    textarea, input {{
        background-color: rgba(15, 23, 42, 0.8) !important;
        color: #ffffff !important;
        font-size: 19px !important;
        line-height: 1.6 !important;
        border: 2px solid rgba(56, 189, 248, 0.3) !important;
        backdrop-filter: blur(8px);
        border-radius: 8px !important;
        padding: 12px !important;
    }}
    
    textarea:focus, input:focus {{
        border-color: #38bdf8 !important;
    }}
</style>
""", unsafe_allow_html=True)

# 1. High Visibility Header
st.markdown("""
<div class="saas-header-inline">
    <span class="nav-brand-text">⚡ Sentix AI Platform</span>
</div>
""", unsafe_allow_html=True)

if "current_page" not in st.session_state:
    st.session_state.current_page = "Research"

# Horizontal Route Mapper
nav_cols = st.columns([1.1, 1.1, 1.1, 1.3, 1.1, 4.2])
pages = ["Research", "Assistant", "Analytics", "Comparisons", "Contact"]
icons = ["🔬 ", "🤖 ", "📊 ", "🔀 ", "📞 "]

for i, page in enumerate(pages):
    with nav_cols[i]:
        is_active = st.session_state.current_page == page
        if st.button(f"{icons[i]}{page}", key=f"nav_btn_{page}", use_container_width=True, type="primary" if is_active else "secondary"):
            st.session_state.current_page = page
            st.rerun()

st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

# Hero Module with high contrast, crisp text sizing
st.markdown(
    """
    <div style="
        background-image: linear-gradient(rgba(11, 15, 25, 0.75), rgba(7, 10, 19, 0.9)), url('https://images.unsplash.com/photo-1451187580459-43490279c0fa');
        background-size: cover;
        background-position: center;
        border-radius: 14px;
        padding: 40px;
        border: 2px solid rgba(56, 189, 248, 0.25);
        margin-bottom: 40px;
        box-shadow: 0 12px 48px rgba(0,0,0,0.5);
    ">
        <p style="font-size: 14px !important; color: #38bdf8; font-weight: 800; margin: 0 0 8px 0; letter-spacing: 2px; text-transform: uppercase;">Sentiment-Aware Response Platform</p>
        <h1 style="margin: 0 0 12px 0; font-size: 44px !important; font-weight: 900; color: #ffffff !important; letter-spacing: -0.5px;">Sentix AI Engine</h1>
        <p style="font-size: 20px !important; line-height: 1.7 !important; color: #f1f5f9 !important; margin: 0; max-width: 950px; font-weight: 500;">
            Built as an active research trial at IIT Indore. This system helps support staff review text trends, write answers instantly, and look up answers from data guides to help customers faster.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Route execution logic
if st.session_state.current_page == "Research":
    render_research_view()
elif st.session_state.current_page == "Assistant":
    render_assistant_view()
elif st.session_state.current_page == "Analytics":
    render_analytics_view()
elif st.session_state.current_page == "Comparisons":
    render_comparison_view()
elif st.session_state.current_page == "Contact":
    render_contact_view()