import streamlit as st

def feature_card(title, description):
    st.markdown(
        f"""
        <div style="
            background: white;
            padding: 24px;
            border-radius: 16px;
            border-left: 5px solid #D4A017;
            border-top: 1px solid #E2E8F0;
            border-right: 1px solid #E2E8F0;
            border-bottom: 1px solid #E2E8F0;
            margin-bottom: 18px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.02);
            transition: transform 0.3s ease;
        " onmouseover="this.style.transform='translateX(4px)'" onmouseout="this.style.transform='translateX(0)'">
            <h4 style="margin: 0 0 6px 0; color: #071B4D; font-weight: 700; font-size: 16px; letter-spacing:-0.2px;">{title}</h4>
            <p style="margin: 0; color: #64748B; font-size: 14px; line-height: 1.55;">{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )