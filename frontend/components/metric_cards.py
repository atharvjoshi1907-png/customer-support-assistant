import streamlit as st

def metric_cards():
    st.markdown("""
    <style>
    @keyframes countIn {
        from { opacity: 0; transform: scale(0.96); }
        to { opacity: 1; transform: scale(1); }
    }
    [data-testid="stMetric"] {
        background: white !important;
        padding: 20px 25px !important;
        border-radius: 16px !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.02) !important;
        animation: countIn 0.5s ease-out forwards;
        transition: all 0.3s ease;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 30px rgba(7, 27, 77, 0.06) !important;
        border-color: #D4A017 !important;
    }
    [data-testid="stMetricValue"] {
        font-size: 32px !important;
        font-weight: 800 !important;
        color: #071B4D !important;
    }
    [data-testid="stMetricLabel"] {
        font-size: 12px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.8px !important;
        color: #64748B !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Models Monitored", "3 Models")
    with c2: st.metric("System Accuracy", "88.4%")
    with c3: st.metric("Mean Latency", "0.42s")
    with c4: st.metric("Evaluation Sets", "500+")