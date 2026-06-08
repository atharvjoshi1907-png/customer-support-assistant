import streamlit as st

def feature_card(title, description):
    st.markdown(
        f"""
        <style>
            .feature-container {{
                padding: 22px;
                border-radius: 12px;
                border: 1px solid rgba(56, 189, 248, 0.12);
                background: rgba(15, 23, 42, 0.6);
                backdrop-filter: blur(8px);
                transition: all 0.25s ease;
            }}
            .feature-container:hover {{
                transform: translateY(-3px);
                border-color: rgba(56, 189, 248, 0.3);
            }}
        </style>
        <div class="feature-container">
            <h4 style="margin: 0 0 8px 0; font-size: 18px; font-weight: 700; color: #38bdf8 !important;">{title}</h4>
            <p style="margin: 0; font-size: 14.5px; line-height: 1.5; color: #cbd5e1 !important; opacity: 0.95;">{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )