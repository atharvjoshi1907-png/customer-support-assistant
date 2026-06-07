import streamlit as st

def reply_card(text_payload):
    """Renders system generated response scripts inside text workspace blocks."""
    st.markdown(f"""
    <div style="background-color: #f0fdf4; border: 1px solid #dcfce7; padding: 16px; 
                border-radius: 8px; font-size: 14px; color: #166534; line-height: 1.6;">
        {text_payload}
    </div>
    """, unsafe_allow_html=True)