import streamlit as st

def show_reply_card(result):

    st.markdown("---")

    st.subheader("📩 Generated Response")

    st.write(result["generated_reply"])

    st.subheader("😊 Sentiment")

    st.info(result["sentiment"])

    st.subheader("⚙️ Technique Used")

    st.success(result["technique_used"])