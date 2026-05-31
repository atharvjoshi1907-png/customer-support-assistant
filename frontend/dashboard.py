import streamlit as st

st.set_page_config(
    page_title="Customer Support Assistant",
    layout="wide"
)

st.title("🤖 Customer Support Assistant")

st.markdown(
    """
### AI Powered Customer Support System

This project demonstrates:

- Customer Reply Generation
- Sentiment Analysis
- Model Comparison
- Evaluation Dashboard
- Rule Based Responses
- Retrieval Based Responses
"""
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Models",
        "3"
    )

with col2:

    st.metric(
        "Backend",
        "Online"
    )

with col3:

    st.metric(
        "Phase",
        "1"
    )

st.markdown("---")

st.success(
    "Select a page from the sidebar."
)