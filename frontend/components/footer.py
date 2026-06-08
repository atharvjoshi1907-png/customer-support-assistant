import streamlit as st

def render_footer():
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; padding: 10px; color: #cbd5e1; font-size: 14px; opacity: 0.7;">
            © 2026 Sentix AI Platform • Active Research Cluster Pipeline • IIT Indore
        </div>
        """,
        unsafe_allow_html=True
    )