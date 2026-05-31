import streamlit as st

from components.metric_chart import (
    show_accuracy_chart,
    show_latency_chart
)

st.title("📈 Metrics Dashboard")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Accuracy",
        "88%"
    )

with col2:

    st.metric(
        "Latency",
        "0.4 sec"
    )

st.subheader("Model Accuracy")

show_accuracy_chart()

st.subheader("Response Latency")

show_latency_chart()