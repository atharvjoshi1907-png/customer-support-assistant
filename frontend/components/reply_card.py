import streamlit as st

def render_reply(response, sentiment="Polite / Calm", confidence="95% Confident"):
    st.markdown(
        f"""
        <style>
            .reply-wrapper {{
                padding: 26px;
                border-radius: 14px;
                border: 1px solid rgba(16, 185, 129, 0.2);
                border-left: 5px solid #10b981;
                background: rgba(15, 23, 42, 0.65);
                backdrop-filter: blur(10px);
                margin-bottom: 20px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.25);
            }}
        </style>
        <div class="reply-wrapper">
            <h3 style="margin-top:0; font-size:20px; font-weight:700; color: #ffffff !important; letter-spacing: -0.3px;">Vector Completion Result</h3>
            <p style="font-size:15.5px; line-height:1.6; color:#e2e8f0 !important; margin-bottom:14px;">{response}</p>
            <hr style="border:0; border-top:1px solid rgba(255, 255, 255, 0.08); margin:14px 0;">
            <div style="font-size:14px; color:#cbd5e1 !important;">
                <span><b>Identified Sentiment Class:</b> <code style="color:#10b981; background:transparent; font-size:14px;">{sentiment}</code></span><br>
                <span style="display:block; margin-top:4px;"><b>Weight Confidence Factor:</b> <code style="color:#38bdf8; background:transparent; font-size:14px;">{confidence}</code></span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )