import streamlit as st

def render_reply(response, sentiment="Polite / Calm", confidence="95% Confident"):
    # Clear out any potential raw string wrapping bugs
    card_html = f"""
    <div style="
        padding: 24px;
        border-radius: 12px;
        border: 1px solid rgba(16, 185, 129, 0.25);
        border-left: 5px solid #10b981;
        background-color: rgba(15, 23, 42, 0.65);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        margin-bottom: 20px;
    ">
        <h3 style="margin-top: 0; margin-bottom: 12px; font-size: 19px; font-weight: 700; color: #ffffff !important;">
            Vector Completion Result
        </h3>
        <p style="font-size: 15px; line-height: 1.6; color: #e2e8f0 !important; margin-bottom: 16px;">
            {response}
        </p>
        <hr style="border: 0; border-top: 1px solid rgba(255, 255, 255, 0.08); margin: 14px 0;">
        <div style="font-size: 13.5px; color: #cbd5e1 !important; line-height: 1.5;">
            <b>Identified Sentiment Class:</b> <span style="color: #10b981; font-weight: 600;">{sentiment}</span><br>
            <span style="display: block; margin-top: 4px;"><b>Weight Confidence Factor:</b> <span style="color: #38bdf8; font-weight: 600;">{confidence}</span></span>
        </div>
    </div>
    """
    # Force Streamlit to process the visual container markup instead of raw text strings
    st.markdown(card_html, unsafe_allow_html=True)