import streamlit as st
from streamlit_option_menu import option_menu

from views.assistant import render_assistant_view
from views.comparisons import render_comparison_view
from views.analytics import render_analytics_view
from views.research import render_research_view
from views.team import render_team_view
from views.contact import render_contact_view
from components.footer import footer


st.set_page_config(
    page_title="SupportAI | IIT Indore",
    page_icon="◎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Home"

try:
    requested_tab = st.query_params.get("tab")
    if (
        requested_tab in ["Home", "Assistant", "Comparison", "Analytics", "Research", "Team", "Contact"]
        and st.session_state.get("_last_query_tab") != requested_tab
    ):
        st.session_state.active_tab = requested_tab
        st.session_state._last_query_tab = requested_tab
except AttributeError:
    pass

st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --navy: #071936;
        --navy-2: #0b2346;
        --gold: #d5a21a;
        --gold-light: #edbd36;
        --text: #12213c;
        --muted: #5d6b7e;
        --line: #e8edf4;
        --card: #ffffff;
        --blue: #2f78d6;
        --bg: #ffffff;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    #MainMenu, footer, header, [data-testid="stSidebar"] {
        display: none !important;
        visibility: hidden !important;
    }

    .stApp {
        background: var(--bg);
    }

    .block-container {
        max-width: 100% !important;
        padding: 0 !important;
    }

    div[data-testid="stVerticalBlock"] {
        gap: 0;
    }

    h1, h2, h3, h4, p {
        letter-spacing: 0 !important;
    }

    .top-shell {
        background: var(--navy);
        height: 64px;
        border-bottom: 1px solid rgba(255,255,255,.1);
        display: flex;
        align-items: center;
        padding: 0 28px;
        box-shadow: 0 2px 10px rgba(7,25,54,.22);
        position: sticky;
        top: 0;
        z-index: 100;
    }

    .brand {
        color: #fff;
        font-size: 17px;
        font-weight: 800;
        display: flex;
        align-items: center;
        gap: 9px;
        white-space: nowrap;
        flex-shrink: 0;
    }

    .brand-mark {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        border: 2px solid rgba(255,255,255,.75);
        display: inline-grid;
        place-items: center;
        font-size: 14px;
    }

    .nav-wrap {
        flex: 1;
        display: flex;
        justify-content: flex-end;
        margin-left: auto;
        align-items: center;
        gap: 18px;
    }

    .navbar {
    display: flex;
    align-items: center;
    gap: 28px;
    }

    .nav-link {
        color: rgba(255,255,255,0.75);
        text-decoration: none;
        font-size: 15px;
        font-weight: 700;
        padding: 22px 0;
        transition: all 0.2s ease;
        border-bottom: 3px solid transparent;
    }

    .nav-link:hover {
        color: white;
    }

    .active-nav {
        color: #d5a21a !important;
        border-bottom: 3px solid #d5a21a;
    }
    
    .nav-cta {
        margin-left: 18px;
        background: transparent !important;
        border: 2px solid rgba(255,255,255,.5) !important;
        color: #fff !important;
        border-radius: 6px !important;
        padding: 7px 16px !important;
        font-size: 13px !important;
        font-weight: 700 !important;
        white-space: nowrap !important;
        text-decoration: none !important;
        line-height: 1.2;
    }

    .page-pad {
        padding: 46px 44px 44px;
    }

    .page-title {
        color: var(--text);
        font-size: 32px;
        line-height: 1.15;
        margin: 0 0 8px;
        font-weight: 800;
    }

    .page-subtitle {
        color: var(--muted);
        font-size: 15px;
        font-weight: 500;
        margin: 0 0 36px;
    }

    .card {
        background: var(--card);
        border: 1px solid var(--line);
        border-radius: 8px;
        box-shadow: 0 4px 18px rgba(16, 33, 60, .07);
    }

    .gold-button {
        background: linear-gradient(180deg, #edbd36, #d69d14);
        color: #fff;
        border: 0;
        border-radius: 8px;
        padding: 14px 24px;
        font-weight: 800;
        font-size: 14px;
        display: inline-flex;
        align-items: center;
        gap: 10px;
        box-shadow: 0 9px 18px rgba(213,162,26,.24);
    }

    .ghost-button {
        color: #fff;
        border: 2px solid rgba(255,255,255,.42);
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 800;
        font-size: 14px;
        background: rgba(255,255,255,.04);
        display: inline-flex;
        align-items: center;
        gap: 8px;
    }

    .gold-button, .ghost-button {
        text-decoration: none !important;
    }

    .stButton > button {
        background: linear-gradient(180deg, #edbd36, #d69d14) !important;
        color: #fff !important;
        border: 0 !important;
        border-radius: 8px !important;
        min-height: 52px !important;
        font-weight: 800 !important;
        box-shadow: 0 8px 16px rgba(213,162,26,.2) !important;
    }

    .stTextArea textarea, .stTextInput input {
        border: 1px solid var(--line) !important;
        border-radius: 8px !important;
        background: #fff !important;
        color: var(--text) !important;
        font-size: 14px !important;
        resize: none !important;
    }

    @media (max-width: 760px) {
        .top-shell {
            padding: 0 16px;
            flex-direction: column;
            align-items: flex-start;
            min-height: auto;
        }
        .brand {
            padding-top: 18px;
        }
        .nav-wrap {
            margin-left: 0;
            width: 100%;
            overflow-x: auto;
        }
        div[data-testid="stRadio"] div[role="radiogroup"] {
            justify-content: flex-start !important;
            gap: 16px !important;
        }
        .page-pad {
            padding: 32px 20px;
        }
    }
</style>
""",
    unsafe_allow_html=True,
)

tabs_list = [
    "Home",
    "Assistant",
    "Comparison",
    "Analytics",
    "Research",
    "Team",
    "Contact",
]

selected_tab = option_menu(
    menu_title=None,
    options=tabs_list,
    orientation="horizontal",
    default_index=tabs_list.index(st.session_state.active_tab),
    styles={
        "container": {
            "background-color": "#071936",
            "padding": "0!important",
        },
        "icon": {
            "display": "none",
        },
        "nav-link": {
            "font-size": "15px",
            "font-weight": "600",
            "color": "white",
            "text-align": "center",
        },
        "nav-link-selected": {
            "background-color": "#d5a21a",
            "color": "white",
        },
    },
)



if selected_tab != st.session_state.active_tab:
    st.session_state.active_tab = selected_tab
    st.rerun()



if st.session_state.active_tab == "Home":
    st.markdown(
        """
<section class="home-hero">
    <div class="hero-copy">
        <div class="hero-kicker">IIT INDORE</div>
        <h1>SupportAI</h1>
        <h2>Sentiment-Aware Customer<br>Support Assistant</h2>
        <p>A research initiative exploring and comparing multiple response generation strategies for customer support automation using advanced NLP techniques.</p>
        <div class="hero-actions">
            <a class="gold-button" href="?tab=Assistant" target="_self">Launch Assistant <span>→</span></a>
            <a class="ghost-button" href="?tab=Research" target="_self">View Research <span>◎</span></a>
        </div>
    </div>
    <div class="brain-scene" aria-hidden="true">
        <div class="orbit"></div>
        <div class="brain-wrap">
            <div class="brain">
                <div class="brain-line l1"></div>
                <div class="brain-line l2"></div>
                <div class="brain-line l3"></div>
                <div class="brain-line l4"></div>
                <div class="spark s1"></div>
                <div class="spark s2"></div>
                <div class="spark s3"></div>
            </div>
            <div class="bubble bubble-a"></div>
            <div class="bubble bubble-b"></div>
            <div class="bubble bubble-c"></div>
        </div>
    </div>
</section>
<style>
    .home-hero {
        min-height: 600px;
        background:
            radial-gradient(circle at 76% 38%, rgba(53,113,213,.25), transparent 28%),
            radial-gradient(circle at 20% 10%, rgba(33,78,142,.28), transparent 32%),
            linear-gradient(135deg, #071936 0%, #061228 100%);
        color: #fff;
        display: grid;
        grid-template-columns: minmax(0, 1.05fr) minmax(340px, .95fr);
        align-items: center;
        gap: 20px;
        padding: 60px 68px;
        overflow: hidden;
    }

    .hero-kicker {
        color: var(--gold);
        font-size: 20px;
        font-weight: 800;
        margin-bottom: 22px;
        letter-spacing: .5px;
    }

    .hero-copy h1 {
        color: #fff !important;
        font-size: 58px;
        line-height: 1;
        margin: 0 0 16px;
        font-weight: 800;
    }

    .hero-copy h2 {
        color: #fff !important;
        font-size: 35px;
        line-height: 1.22;
        margin: 0;
        font-weight: 800;
    }

    .hero-copy p {
        color: rgba(255,255,255,.82);
        max-width: 520px;
        font-size: 18px;
        line-height: 1.6;
        margin: 34px 0 32px;
        font-weight: 500;
    }

    .hero-actions {
        display: flex;
        gap: 16px;
        flex-wrap: wrap;
    }

    .brain-scene {
        position: relative;
        min-height: 370px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .orbit {
        position: absolute;
        inset: 30px 20px 30px 20px;
        border: 2px solid rgba(63,125,229,.22);
        border-radius: 50%;
        transform: rotate(-9deg);
    }

    .brain-wrap {
        position: relative;
        width: 310px;
        height: 220px;
        margin-top: 20px;
    }

    .brain {
        position: relative;
        width: 310px;
        height: 215px;
        border: 5px solid #5d8fe8;
        border-radius: 48% 52% 42% 44%;
        box-shadow: 0 0 0 8px rgba(73,125,224,.13), 0 0 55px rgba(82,139,245,.4);
        background: rgba(23,55,117,.45);
        overflow: visible;
    }

    .brain:after {
        content: "";
        position: absolute;
        width: 74px;
        height: 88px;
        right: 52px;
        bottom: -52px;
        border-right: 5px solid #5d8fe8;
        border-bottom: 5px solid #5d8fe8;
        border-radius: 0 0 36px 0;
        transform: rotate(13deg);
    }

    .brain-line {
        position: absolute;
        background: rgba(126,169,255,.85);
        height: 4px;
        border-radius: 999px;
        box-shadow: 0 0 10px rgba(126,169,255,.8);
    }

    .l1 { width: 195px; left: 44px; top: 56px; }
    .l2 { width: 155px; left: 70px; top: 104px; transform: rotate(10deg); }
    .l3 { width: 108px; left: 42px; top: 148px; transform: rotate(-12deg); }
    .l4 { width: 4px; height: 118px; left: 150px; top: 22px; }

    .spark {
        position: absolute;
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: #fff;
        box-shadow: 0 0 18px 7px rgba(99,152,255,.85);
    }

    .s1 { left: 36px; top: 48px; }
    .s2 { left: 143px; top: 14px; }
    .s3 { right: 44px; bottom: 48px; }

    .bubble {
        position: absolute;
        width: 100px;
        height: 60px;
        border-radius: 8px;
        background: rgba(28,67,134,.68);
        box-shadow: 0 0 24px rgba(32,84,166,.22);
    }

    .bubble:before, .bubble:after {
        content: "";
        position: absolute;
        left: 16px;
        right: 18px;
        height: 4px;
        background: rgba(111,163,255,.65);
        border-radius: 999px;
    }

    .bubble:before { top: 20px; }
    .bubble:after { top: 34px; right: 36px; }
    .bubble-a { right: -10px; top: 60px; }
    .bubble-b { right: -8px; bottom: 60px; }
    .bubble-c { left: -10px; bottom: 10px; }

    @media (max-width: 860px) {
        .home-hero {
            grid-template-columns: 1fr;
            padding: 42px 26px;
        }
        .hero-copy h1 { font-size: 46px; }
        .hero-copy h2 { font-size: 30px; }
        .hero-copy p { font-size: 17px; }
        .brain-scene { min-height: 300px; transform: scale(.82); transform-origin: left top; }
    }
</style>
""",
        unsafe_allow_html=True,
    )
elif st.session_state.active_tab == "Assistant":
    render_assistant_view()
elif st.session_state.active_tab == "Comparison":
    render_comparison_view()
elif st.session_state.active_tab == "Analytics":
    render_analytics_view()
elif st.session_state.active_tab == "Research":
    render_research_view()
elif st.session_state.active_tab == "Team":
    render_team_view()
elif st.session_state.active_tab == "Contact":
    render_contact_view()

footer()