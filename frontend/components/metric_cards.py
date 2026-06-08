import streamlit as st

def render_metrics():
    st.markdown("""
    <style>
        div[data-testid="stMetric"] {
            padding: 22px !important;
            border-radius: 12px !important;
            border: 1px solid rgba(56, 189, 248, 0.12) !important;
            background: rgba(15, 23, 42, 0.6) !important;
            backdrop-filter: blur(8px);
            transition: all 0.25s ease !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        }
        div[data-testid="stMetric"]:hover { 
            transform: translateY(-4px) !important; 
            border-color: rgba(56, 189, 248, 0.3) !important;
            box-shadow: 0 6px 24px rgba(56, 189, 248, 0.1);
        }
        div[data-testid="stMetricLabel"], div[data-testid="stMetricValue"] {
            color: #ffffff !important;
        }
    </style>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Answer Accuracy", "94.2%")
    with c2: st.metric("Reply Time", "0.24 seconds")
    with c3: st.metric("Total Solved Tickets", "1,420+")
    with c4: st.metric("Active Training Steps", "4 Done")