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
        opacity: 0.03;
        pointer-events: none;
        z-index: 1;
    }}
    """

# Google Stitch Inspired Deep Space Grid Styling with Blended Clean Header Architecture
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
        color: #f8fafc !important;
    }}
    
    /* Remove default top padding added by Streamlit block structure */
    .block-container {{
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }}
    
    {logo_watermark_style}

    /* Core Page Entry Shift Animation Blueprint */
    @keyframes stitchFadeEntrance {{
        0% {{ opacity: 0; transform: translateY(12px); filter: blur(3px); }}
        100% {{ opacity: 1; transform: translateY(0); filter: blur(0); }}
    }}
    
    /* Bind animation cleanly to content container views */
    [data-testid="stVerticalBlock"] > div {{
        animation: stitchFadeEntrance 0.45s cubic-bezier(0.16, 1, 0.3, 1) both;
    }}

    /* Global Containment Fix: Nukes any stray white background components */
    div[data-testid="stVerticalBlock"], 
    div[data-testid="element-container"], 
    .element-container,
    div[data-class="stMarkdownContainer"] {{
        background-color: transparent !important;
    }}

    /* Clean Integrated Header Branding Block */
    .saas-header-inline {{
        padding: 0 0 10px 0;
        margin-bottom: 20px;
        border-bottom: 1px solid rgba(56, 189, 248, 0.15);
    }}

    .nav-brand-text {{
        font-size: 26px;
        font-weight: 800;
        color: #38bdf8;
        letter-spacing: -0.5px;
    }}

    /* Seamless Row Navigation Overrides */
    div[data-testid="stHorizontalBlock"] {{
        background: transparent !important;
        padding: 0 !important;
        align-items: center !important;
        margin-bottom: 30px !important;
    }}

    /* Frameless Navigation Links Interface Style */
    div.stButton > button {{
        background-color: transparent !important;
        color: #cbd5e1 !important;
        border: none !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        transition: all 0.2s ease-in-out !important;
        border-radius: 6px !important;
        padding: 6px 14px !important;
        cursor: pointer !important;
        text-align: left !important;
    }}
    
    /* Elegant Underline-Glow Hover Accent Simulation */
    div.stButton > button:first-child:hover,
    div.stButton > button:hover {{
        background-color: rgba(56, 189, 248, 0.08) !important;
        color: #38bdf8 !important;
        transform: translateY(-1px) !important;
        box-shadow: none !important;
    }}
    
    /* Typography color force mappings on hover states */
    div.stButton > button:hover p,
    div.stButton > button:hover span,
    div.stButton > button:hover div {{
        color: #38bdf8 !important;
    }}
    
    /* Clean Active Text Link Indicator Architecture */
    div.stButton > button[data-testid="baseButton-primary"] {{
        background-color: rgba(56, 189, 248, 0.12) !important;
        color: #38bdf8 !important;
        font-weight: 700 !important;
        border: 1px solid rgba(56, 189, 248, 0.25) !important;
        box-shadow: 0 2px 10px rgba(56, 189, 248, 0.1) !important;
    }}
    
    div.stButton > button[data-testid="baseButton-primary"]:hover {{
        background-color: rgba(56, 189, 248, 0.18) !important;
    }}

    /* Global Typography Rules */
    h1, h2, h3, h4, h5, h6, p, span, label, [data-testid="stWidgetLabel"] {{
        color: #f8fafc !important;
    }}
    
    /* Text input textareas dark theme validation framing */
    textarea, input {{
        background-color: rgba(15, 23, 42, 0.6) !important;
        color: #f8fafc !important;
        border: 1px solid rgba(56, 189, 248, 0.2) !important;
        backdrop-filter: blur(8px);
        border-radius: 8px !important;
    }}
</style>
""", unsafe_allow_html=True)

# 1. Inline Blended Navbar Header Brand
st.markdown("""
<div class="saas-header-inline">
    <span class="nav-brand-text">⚡ Sentix AI</span>
</div>
""", unsafe_allow_html=True)

# 2. Page Switch Routing Initialization
if "current_page" not in st.session_state:
    st.session_state.current_page = "Research"

# Horizontal Navigation Links Row Directly Below Brand Title Line
nav_cols = st.columns([1, 1, 1, 1.2, 1, 5])
pages = ["Research", "Assistant", "Analytics", "Comparisons", "Contact"]
icons = ["🔬 ", "🤖 ", "📊 ", "🔀 ", "📞 "]

for i, page in enumerate(pages):
    with nav_cols[i]:
        is_active = st.session_state.current_page == page
        if st.button(f"{icons[i]}{page}", key=f"nav_btn_{page}", use_container_width=True, type="primary" if is_active else "secondary"):
            st.session_state.current_page = page
            st.rerun()

# 3. Top Earth Hero Module Block Setup
st.markdown(
    """
    <div style="
        background-image: linear-gradient(rgba(11, 15, 25, 0.65), rgba(7, 10, 19, 0.85)), url('https://images.unsplash.com/photo-1451187580459-43490279c0fa');
        background-size: cover;
        background-position: center;
        border-radius: 14px;
        padding: 36px;
        border: 1px solid rgba(56, 189, 248, 0.15);
        margin-bottom: 35px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.4);
    ">
        <p style="font-size: 11px; color: #38bdf8; font-weight: 700; margin: 0 0 6px 0; letter-spacing: 2px;">SENTIMENT-AWARE RESPONSE PLATFORM</p>
        <h1 style="margin: 0 0 6px 0; font-size: 36px; font-weight: 800; color: #ffffff !important; letter-spacing: -0.5px;">Sentix AI Engine</h1>
        <p style="font-size: 15px; line-height: 1.6; color: #cbd5e1 !important; margin: 0; max-width: 850px; opacity: 0.9;">
            Built as an active research trial at IIT Indore. This system helps support staff review text trends, write answers instantly, and look up answers from data guides to help customers faster.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Render View Components
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