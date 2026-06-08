import streamlit as st
from components.metric_cards import render_metrics
from components.feature_card import feature_card
from components.footer import render_footer

def render_research_view():
    render_metrics()
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("<h2 style='font-weight: 800; margin-bottom: 4px; letter-spacing: -0.5px;'>How the AI Learns</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #cbd5e1; opacity: 0.8; margin-bottom: 25px; font-size: 16px;'>We tested different ways to train our AI model to find the best balance of speed and helpfulness.</p>", unsafe_allow_html=True)

    st.markdown("""
    <style>
        .tech-box {
            padding: 22px;
            border-radius: 12px;
            font-weight: 600;
            font-size: 16px;
            text-align: center;
            border: 1px solid rgba(56, 189, 248, 0.15);
            border-left: 5px solid #38bdf8;
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(8px);
            color: #ffffff;
            transition: all 0.25s ease;
        }
        .tech-box:hover { 
            transform: translateY(-4px); 
            border-color: rgba(56, 189, 248, 0.35);
            box-shadow: 0 4px 20px rgba(56, 189, 248, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown('<div class="tech-box">⚡ Full fine-tuning</div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="tech-box">⚙️ LoRA</div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="tech-box">🧠 QLoRA</div>', unsafe_allow_html=True)
    with m4: st.markdown('<div class="tech-box">🎯 Prompt Tuning</div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    left, right = st.columns([1.2, 1])

    with left:
        st.markdown("<h2 style='font-weight: 800; margin-bottom: 18px; letter-spacing: -0.5px;'>Our Design Scope</h2>", unsafe_allow_html=True)
        feature_card("🛡️ Safe and Correct Answers", "We evaluate models using validation loss, perplexity, and BLEU score check matching.")
        st.markdown("<br>", unsafe_allow_html=True)
        feature_card("🚀 Fine-Tuned Optimization", "Track trainable parameters, memory use, and training timelines flawlessly.")

    with right:
        st.markdown("<h2 style='font-weight: 800; margin-bottom: 18px; letter-spacing: -0.5px;'>System Pipeline Processing</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div style="padding: 22px; border-radius: 12px; border: 1px dashed rgba(56, 189, 248, 0.25); background: rgba(15, 23, 42, 0.5); backdrop-filter: blur(8px); color: #38bdf8;">
            <code style="font-size: 14px; color: inherit; display:block; line-height: 1.7; background: transparent; font-family: monospace;">
                <b>Step 1:</b> User inputs targeted support text query<br>
                <b>Step 2:</b> Frontend routes packets down Flask backend API endpoint<br>
                <b>Step 3:</b> Engine feeds variables through running fine-tuned model<br>
                <b>Step 4:</b> Side-by-side array logic compares variant weights outputs<br>
                <b>Step 5:</b> Dashboard updates loss curves visually
            </code>
        </div>
        """, unsafe_allow_html=True)
        st.progress(100)

    render_footer()