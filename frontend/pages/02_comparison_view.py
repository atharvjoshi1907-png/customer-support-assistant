import streamlit as st
import pandas as pd

st.title("📊 Model Comparison")

data = pd.DataFrame(
    {
        "Message": [
            "Order delayed",
            "Need refund",
            "Damaged product"
        ],
        "Baseline": [
            "Generic response",
            "Generic response",
            "Generic response"
        ],
        "Rule Based": [
            "Delay policy",
            "Refund policy",
            "Replacement policy"
        ],
        "Retrieval": [
            "Specific answer",
            "Specific answer",
            "Specific answer"
        ]
    }
)

st.dataframe(
    data,
    use_container_width=True
)