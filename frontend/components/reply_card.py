import streamlit as st
import re

def render_reply(response, sentiment="Polite / Calm", confidence="95% Confident"):

    # Remove HTML tags coming from backend
    clean_response = re.sub(r"<[^>]+>", "", str(response))

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
            <h3 style="margin-top:0; font-size:20px; font-weight:700; color:#ffffff;">
                Vector Completion Result
            </h3>

            <p style="font-size:15px; line-height:1.8; color:#e2e8f0;">
                {clean_response}
            </p>

            <hr style="border:0; border-top:1px solid rgba(255,255,255,0.08); margin:14px 0;">

            <div style="font-size:14px; color:#cbd5e1;">
                <b>Identified Sentiment Class:</b>
                <span style="color:#10b981;">{sentiment}</span>
                <br><br>

                <b>Weight Confidence Factor:</b>
                <span style="color:#38bdf8;">{confidence}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )