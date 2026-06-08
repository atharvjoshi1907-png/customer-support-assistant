import streamlit as st
from components.footer import render_footer

def render_team():
    st.markdown("<h1 style='font-weight: 800; margin-bottom: 10px;'>System Engineering Core</h1>", unsafe_allow_html=True)
    st.markdown("""
    <style>
        .team-tech-card {
            padding: 30px;
            border-radius: 14px;
            border-top: 4px solid #6366f1;
            box-shadow: 0 10px 30px rgba(0,0,0,0.01);
            transition: all 0.25s ease;
        }
        .team-tech-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(79, 70, 229, 0.08);
        }
        .team-tech-card h3 { margin-top: 0 !important; font-size: 24px !important; font-weight: 700 !important; }
        .uid-tag { font-family: monospace; font-size: 14px !important; color: #6366f1; font-weight: 600; }
        
        @media (prefers-color-scheme: dark) { .team-tech-card { background: #1e293b; } }
        @media (prefers-color-scheme: light) { .team-tech-card { background: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #6366f1; } }
    </style>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="team-tech-card">
            <span class="uid-tag">ENG_NODE_01</span>
            <h3>Atharv Joshi</h3>
            <p style="margin: 5px 0 15px 0; font-weight: 600; color: #4f46e5;">Lead Pipeline Architect</p>
            <p style="font-size: 16px !important; line-height: 1.6;">Responsible for managing tensor vector pipelines, quantization pathways, and cluster distribution logic loops.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="team-tech-card">
            <span class="uid-tag">ENG_NODE_02</span>
            <h3>Drishti</h3>
            <p style="margin: 5px 0 15px 0; font-weight: 600; color: #4f46e5;">Interface Systems Engineer</p>
            <p style="font-size: 16px !important; line-height: 1.6;">Maintains real-time canvas configuration styles, responsive variable scripts, and high-fidelity tracking layouts.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="team-tech-card">
            <span class="uid-tag">GUIDE_NODE_00</span>
            <h3>Prof. Abhishek</h3>
            <p style="margin: 5px 0 15px 0; font-weight: 600; color: #4f46e5;">Academic Systems Supervisor</p>
            <p style="font-size: 16px !important; line-height: 1.6;">Directs architectural verification testing methodologies, proof validation models, and deep learning integrity reports.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight: 800; margin-bottom: 20px;'>Pipeline Functional Overhaul Areas</h3>", unsafe_allow_html=True)

    # Hover Adaptive Structural Blocks
    st.markdown("""
    <style>
        .resp-bar { padding: 16px 24px; border-radius: 8px; margin-bottom: 12px; font-weight: 600; font-size: 17px; transition: all 0.2s; border-left: 3px solid #10b981; }
        .resp-bar:hover { transform: translateX(6px); }
        @media (prefers-color-scheme: dark) { .resp-bar { background: rgba(16,185,129,0.08); color: #a7f3d0; } }
        @media (prefers-color-scheme: light) { .resp-bar { background: #f0fdf4; color: #166534; } }
    </style>
    <div class="resp-bar">Core Mathematical Weight Configurations</div>
    <div class="resp-bar">Context Embeddings Database Ingestion Validation</div>
    <div class="resp-bar">Multi-Modal Metric Processing Infrastructure Array</div>
    """, unsafe_allow_html=True)

    render_footer()