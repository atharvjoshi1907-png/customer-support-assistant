import streamlit as st

def footer():
    st.markdown("""
    <hr style="border-top: 1px solid #E2E8F0; margin-top: 70px; margin-bottom: 30px;">
    <div style="text-align: center; padding-bottom: 40px; color: #94A3B8; font-size: 13px; line-height:1.6;">
        <h4 style="color: #071B4D; margin-bottom: 6px; font-weight: 800; font-size: 18px; letter-spacing: -0.5px;">⦿ EchoDesk AI</h4>
        Department of Computer Science & Engineering • <b>IIT Indore</b><br>
        <span style="color:#64748B;">Automated Language Intelligence Research Labs Framework</span><br>
        <div style="margin-top: 12px; font-size: 11px; color: #CBD5E1; background:#071B4D; display:inline-block; padding:4px 12px; border-radius:12px;">© 2026 EchoDesk AI. Production Streamlit Mirror.</div>
    </div>
    """, unsafe_allow_html=True)