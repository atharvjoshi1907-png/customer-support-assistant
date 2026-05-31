import streamlit as st
import pandas as pd


def show_accuracy_chart():

    data = pd.DataFrame(
        {
            "Model": [
                "Baseline",
                "Rule Based",
                "Retrieval"
            ],
            "Accuracy": [
                72,
                80,
                88
            ]
        }
    )

    st.bar_chart(
        data.set_index("Model")
    )


def show_latency_chart():

    data = pd.DataFrame(
        {
            "Model": [
                "Baseline",
                "Rule Based",
                "Retrieval"
            ],
            "Latency": [
                2.5,
                0.1,
                0.4
            ]
        }
    )

    st.bar_chart(
        data.set_index("Model")
    )