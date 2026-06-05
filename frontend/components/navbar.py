import streamlit as st

def navbar():
    st.markdown("""
    <style>
    @keyframes slideDown {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    .navbar-container {
        background: #071B4D;
        padding: 14px 40px;
        border-radius: 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(7, 27, 77, 0.2);
        animation: slideDown 0.5s ease-out forwards;
    }
    
    .navbar-logo {
        color: white;
        font-size: 24px;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    
    .nav-col div.stButton > button {
        background: transparent !important;
        color: #94A3B8 !important;
        border: none !important;
        padding: 6px 12px !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        height: auto !important;
        box-shadow: none !important;
        transform: none !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .nav-col div.stButton > button:hover {
        color: #D4A017 !important;
        background: transparent !important;
        transform: translateY(-1px) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    logo_col, nav_col = st.columns([3, 7])
    
    with logo_col:
        st.markdown('<div class="navbar-container"><div class="navbar-logo">⦿ EchoDesk AI</div></div>', unsafe_allow_html=True)
        
    with nav_col:
        tabs = ["Home", "Assistant", "Comparison", "Analytics", "Research", "Team", "Contact"]
        cols = st.columns(len(tabs))
        
        if "active_tab" not in st.session_state:
            st.session_state.active_tab = "Home"
            
        for i, tab_name in enumerate(tabs):
            with cols[i]:
                st.markdown('<div class="nav-col">', unsafe_allow_html=True)
                is_active = st.session_state.active_tab == tab_name
                display_label = f"✨ {tab_name}" if is_active else tab_name
                
                # Active tab styling injection
                if is_active:
                    st.markdown("""<style>
                        [data-testid="stSidebarNav"] + div, div.stButton > button[key*="nav_link_"""+tab_name+""""] {
                            color: #D4A017 !important;
                            font-weight: 700 !important;
                        }
                    </style>""", unsafe_allow_html=True)
                
                if st.button(display_label, key=f"nav_link_{tab_name}"):
                    st.session_state.active_tab = tab_name
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)