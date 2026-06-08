import streamlit as st

def render_metrics():
    st.markdown("""
    <style>
        div[data-testid="stMetric"] {
            padding: 26px !important;
            border-radius: 14px !important;
            border: 2px solid rgba(56, 189, 248, 0.25) !important;
            background: rgba(15, 23, 42, 0.75) !important;
            backdrop-filter: blur(8px);
            box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3);
        }
        div[data-testid="stMetricLabel"] {
            color: #cbd5e1 !important;
            font-size: 18px !important;
            font-weight: 700 !important;
            margin-bottom: 8px !important;
        }
        div[data-testid="stMetricValue"] {
            color: #ffffff !important;
            font-size: 42px !important;
            font-weight: 900 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Answer Accuracy", "94.2%")
    with c2: st.metric("Reply Time", "0.24 sec")
    with c3: st.metric("Solved Tickets", "1,420+")
    with c4: st.metric("Training Steps", "4 Done")