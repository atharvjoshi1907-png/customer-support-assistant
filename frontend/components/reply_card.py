import streamlit as st

def render_reply(response, sentiment="Polite / Calm", confidence="95% Confident"):
    card_html = f"""
    <div style="
        padding: 30px;
        border-radius: 14px;
        border: 2px solid #10b981;
        background-color: rgba(15, 23, 42, 0.85);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    ">
        <h3 style="margin-top: 0; margin-bottom: 16px; font-size: 26px; font-weight: 800; color: #ffffff !important;">
            ✨ Generated Response Draft
        </h3>
        <p style="font-size: 21px !important; line-height: 1.8 !important; color: #ffffff !important; margin-bottom: 20px; font-weight: 500; letter-spacing: 0.2px;">
            {response}
        </p>
        <hr style="border: 0; border-top: 2px solid rgba(255, 255, 255, 0.15); margin: 18px 0;">
        <div style="font-size: 18px !important; color: #e2e8f0 !important; line-height: 1.6;">
            <span style="display: block; margin-bottom: 6px;"><b>Detected Customer Mood:</b> <span style="color: #10b981; font-weight: 800; font-size: 19px;">{sentiment}</span></span>
            <span><b>System Confidence Level:</b> <span style="color: #38bdf8; font-weight: 800; font-size: 19px;">{confidence}</span></span>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)