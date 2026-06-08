import streamlit as st
from components.metric_charts import render_accuracy_chart, render_latency_chart
from components.footer import render_footer
from components.metric_cards import render_metrics

def render_analytics_view():
    st.markdown("<h2 style='font-weight: 800; margin-bottom: 25px; letter-spacing: -0.5px;'>System Performance Logs</h2>", unsafe_allow_html=True)
    
    render_metrics()
    st.markdown("<br><br>", unsafe_allow_html=True)
    left, right = st.columns(2)

    with left:
        st.markdown("<h4 style='font-weight: 700; margin-bottom: 12px;'>Accuracy Scores</h4>", unsafe_allow_html=True)
        render_accuracy_chart()

    with right:
        st.markdown("<h4 style='font-weight: 700; margin-bottom: 12px;'>Waiting Times</h4>", unsafe_allow_html=True)
        render_latency_chart()

    render_footer()