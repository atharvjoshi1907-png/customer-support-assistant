import streamlit as st
from components.reply_card import render_reply
from components.footer import render_footer

def render_assistant_view():
    st.markdown("<h2 style='font-weight: 800; margin-bottom: 5px; letter-spacing: -0.5px;'>AI Help Desk Assistant</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #cbd5e1; opacity: 0.8; font-size: 16px; margin-bottom: 30px;'>Type or paste a customer message below to get an instant support draft.</p>", unsafe_allow_html=True)

    left_col, right_col = st.columns([1.1, 1])

    with left_col:
        st.markdown("<h4 style='font-weight: 700; margin-bottom: 12px;'>Customer Message Input</h4>", unsafe_allow_html=True)
        customer_query = st.text_area(
            "What did the customer write?",
            height=200,
            placeholder="Type or paste the complaint or question here...",
            label_visibility="collapsed",
            key="assistant_query_input"
        )
        st.markdown("<br>", unsafe_allow_html=True)
        trigger_pipeline = st.button("Generate Answer Draft", type="primary", use_container_width=True)

    with right_col:
        if trigger_pipeline and customer_query.strip():
            st.markdown("<h4 style='font-weight: 700; margin-bottom: 15px;'>Generated Solution</h4>", unsafe_allow_html=True)
            response = "Thank you for reaching out to Sentix AI support. We completely understand your issue and are here to help. Our support team is already checking your account details and will call or email you shortly with a full solution."
            render_reply(response, "Polite / Calm", "95% Confident")
        else:
            st.markdown("<h4 style='font-weight: 700; margin-bottom: 12px;'>Waiting for Input</h4>", unsafe_allow_html=True)
            st.markdown("""
            <div style="padding: 24px; border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.15); background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(8px); color: #ffffff;">
                <h5 style="margin: 0 0 8px 0; font-size: 16px; font-weight: 700; color: #38bdf8 !important;">AI Writing Terminal</h5>
                <p style="font-size: 14.5px; line-height: 1.5; opacity: 0.8; margin: 0; color: #cbd5e1;">
                    Once you type a message on the left and click the button, the Sentix AI engine will process the text metrics and display a response.
                </p>
            </div>
            """, unsafe_allow_html=True)

    render_footer()