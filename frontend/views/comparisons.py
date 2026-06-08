import streamlit as st
from components.footer import render_footer

def render_comparison_view():
    st.markdown("<h2 style='font-weight: 800; letter-spacing: -0.5px;'>Compare System Settings</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #cbd5e1; opacity: 0.8; font-size: 16px; margin-bottom: 25px;'>See how different versions of our system perform side-by-side.</p>", unsafe_allow_html=True)

    st.markdown("""
    <style>
        .stTable table { 
            font-size: 15px !important; 
            width: 100% !important; 
            border-radius: 12px !important; 
            overflow: hidden !important; 
            border: 1px solid rgba(56, 189, 248, 0.15) !important;
            background: rgba(15, 23, 42, 0.5) !important;
            backdrop-filter: blur(8px);
        }
        .stTable th { 
            padding: 16px !important; 
            background: rgba(30, 41, 59, 0.8) !important; 
            color: #38bdf8 !important; 
            border-bottom: 2px solid rgba(56, 189, 248, 0.2) !important;
        }
        .stTable td { 
            padding: 16px !important; 
            color: #ffffff !important; 
            border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
        }
    </style>
    """, unsafe_allow_html=True)

    data = {
        "Metric Parameters": ["Validation Loss / Perplexity", "BLEU Evaluation Score", "Trainable Param Weighting", "Inference Timeline Speed"],
        "Old Setup (Baseline)": ["High Loss", "Low Match Score", "Full Weights Bound", "2.5 seconds"],
        "Rule-Based Setup": ["Medium Loss", "Average Match Score", "Manual Arrays Map", "1.1 seconds"],
        "Our Sentix AI Setup": ["Lowest Evaluated Loss", "Highest BLEU Score Match", "PEFT Matrix Tuning Added", "0.24 seconds"]
    }

    st.table(data)
    render_footer()