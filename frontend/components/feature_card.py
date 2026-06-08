import streamlit as st

def feature_card(title, description):
    st.markdown(
        f"""
        <div style="
            padding: 26px;
            border-radius: 12px;
            border: 2px solid rgba(56, 189, 248, 0.2);
            background: rgba(15, 23, 42, 0.65);
            margin-bottom: 16px;
        ">
            <h4 style="margin: 0 0 10px 0; font-size: 22px; font-weight: 800; color: #38bdf8 !important;">{title}</h4>
            <p style="margin: 0; font-size: 18px !important; line-height: 1.7 !important; color: #e2e8f0 !important; font-weight: 500;">{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )