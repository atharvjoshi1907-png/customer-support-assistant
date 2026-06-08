import streamlit as st

def render_footer():
    st.markdown("<br><hr style='border-top: 2px solid rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="text-align: center; padding: 15px; color: #cbd5e1; font-size: 16px; font-weight: 600;">
            © 2026 Sentix AI Platform • Active Research Cluster Pipeline • IIT Indore
        </div>
        """,
        unsafe_allow_html=True
    )