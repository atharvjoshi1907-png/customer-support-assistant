import streamlit as st
import pandas as pd

def accuracy_chart():
    data = pd.DataFrame({
        "Model Strategy": ["Baseline", "Rule-Based", "Retrieval-Augmented"],
        "Accuracy (%)": [72, 80, 88]
    })
    st.bar_chart(data.set_index("Model Strategy"), color="#071B4D", use_container_width=True)

def latency_chart():
    data = pd.DataFrame({
        "Model Strategy": ["Baseline", "Rule-Based", "Retrieval-Augmented"],
        "Latency (s)": [2.5, 0.8, 0.4]
    })
    st.bar_chart(data.set_index("Model Strategy"), color="#D4A017", use_container_width=True)