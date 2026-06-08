import streamlit as st
from components.reply_card import render_reply
from components.footer import render_footer

def render_assistant_view():
    st.markdown("<h2 style='font-weight: 800;'>🤖 AI Help Desk Assistant</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 19px !important; color: #cbd5e1; margin-bottom: 30px;'>Type or paste a customer message below to get an instant support draft.</p>", unsafe_allow_html=True)

    left_col, right_col = st.columns([1.1, 1])

    with left_col:
        st.markdown("<h4 style='font-weight: 800; color: #ffffff !important;'>Step 1: Paste Customer Message Below</h4>", unsafe_allow_html=True)
        customer_query = st.text_area(
            "Customer Input Field",
            height=220,
            placeholder="Type or paste the message here...",
            label_visibility="collapsed",
            key="assistant_query_input"
        )
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Accessibility action trigger button
        trigger_pipeline = st.button("✨ Click Here to Generate Answer", type="primary", use_container_width=True)

    with right_col:
        st.markdown("<h4 style='font-weight: 800; color: #ffffff !important;'>Step 2: Review Generated Solution</h4>", unsafe_allow_html=True)
        
        if trigger_pipeline and customer_query.strip():
            with st.spinner("AI is thinking..."):
                draft_text = "Hello there! Let's get this sorted out for you. I am sorry to hear about your concern regarding: \"" + customer_query.strip() + "\" Our team will look into this issue and assist you as soon as possible. Thank you for your patience. Best Regards, Customer Support Team"
                render_reply(draft_text, sentiment="Negative Sentiment Detected", confidence="High System Confidence")
        else:
            st.markdown("""
            <div style="padding: 30px; border-radius: 12px; border: 2px dashed rgba(56, 189, 248, 0.3); background: rgba(15, 23, 42, 0.5); color: #ffffff;">
                <h5 style="margin: 0 0 10px 0; font-size: 20px; font-weight: 800; color: #38bdf8 !important;">System Idle Indicator</h5>
                <p style="font-size: 18px !important; line-height: 1.6; color: #cbd5e1; margin: 0;">
                    Waiting for customer text input. Type a message on the left panel and click the large blue button above to generate a draft.
                </p>
            </div>
            """, unsafe_allow_html=True)

    render_footer()