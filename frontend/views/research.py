import streamlit as st


def render_research_view():
    st.markdown(
        """
<section class="research-layout">
    <aside class="research-sidebar">
        <div class="side-item active">Problem Statement</div>
        <div class="side-item">Dataset</div>
        <div class="side-item">Methodology</div>
        <div class="side-item">Baseline Model</div>
        <div class="side-item">Rule-Based System</div>
        <div class="side-item">Retrieval-Based System</div>
        <div class="side-item">LoRA Fine-Tuning</div>
        <div class="side-item">QLoRA Fine-Tuning</div>
        <div class="side-item">Evaluation Metrics</div>
        <div class="side-item">Future Work</div>
    </aside>
    <main class="research-content">
        <section class="research-card">
            <div class="statement">
                <h2>Research Statement</h2>
                <p>Customer support teams handle a massive volume of queries daily. Manual responses are time-consuming, inconsistent, and not scalable. There is a need for intelligent systems that can understand customer intent, sentiment, and context to generate accurate and helpful responses automatically.</p>
                <div class="pipeline">
                    <div class="pipe-node"><div class="pipe-icon">🧑</div><div class="pipe-label">Customer<br>Query</div></div>
                    <div class="pipeline-arrow">→</div>
                    <div class="pipe-node"><div class="pipe-icon">🔷</div><div class="pipe-label">NLP Pipeline<br><span class="pipe-sub">(Sentiment + Intent)</span></div></div>
                    <div class="pipeline-arrow">→</div>
                    <div class="pipe-node"><div class="pipe-icon">📋</div><div class="pipe-label">Response<br>Generation</div></div>
                    <div class="pipeline-arrow">→</div>
                    <div class="pipe-node"><div class="pipe-icon">✅</div><div class="pipe-label">Final<br>Response</div></div>
                </div>
            </div>
            <div class="challenge-box">
                <h3>Key Challenges</h3>
                <ul class="challenge-list">
                    <li>Understanding diverse customer intents and sentiments</li>
                    <li>Generating contextually relevant and empathetic responses</li>
                    <li>Comparing multiple response generation strategies</li>
                    <li>Improving performance with parameter-efficient fine-tuning</li>
                </ul>
            </div>
        </section>
    </main>
</section>
<style>
    .research-layout {
        display: grid;
        grid-template-columns: 260px minmax(0, 1fr);
        min-height: 600px;
    }
    .research-sidebar {
        background: linear-gradient(180deg, #0e2848 0%, #112b4a 100%);
        padding: 22px 0;
    }
    .side-item {
        color: rgba(255,255,255,.72);
        font-size: 14px;
        font-weight: 700;
        padding: 13px 28px;
        cursor: pointer;
        transition: background .15s;
    }
    .side-item:hover {
        color: #fff;
    }
    .side-item.active {
        color: #fff;
        background: rgba(255,255,255,.08);
        box-shadow: inset 4px 0 0 var(--gold);
    }
    .research-content {
        padding: 28px 32px 44px;
        background: #fff;
    }
    .research-card {
        border: 1px solid #e8edf4;
        border-radius: 8px;
        box-shadow: 0 4px 18px rgba(16,33,60,.07);
        overflow: hidden;
        max-width: 820px;
    }
    .statement {
        padding: 26px 28px 28px;
    }
    .statement h2 {
        color: #1d2d44;
        font-size: 24px;
        margin: 0 0 14px;
        font-weight: 800;
    }
    .statement p {
        color: #334156;
        font-size: 16px;
        line-height: 1.55;
        margin: 0 0 26px;
        font-weight: 500;
    }
    .pipeline {
        display: grid;
        grid-template-columns: 1fr 30px 1fr 30px 1fr 30px 1fr;
        align-items: center;
        text-align: center;
        gap: 4px;
    }
    .pipeline-arrow {
        color: #506276;
        font-size: 26px;
        font-weight: 800;
    }
    .pipe-node {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
    }
    .pipe-icon {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        display: grid;
        place-items: center;
        color: #2c5d93;
        background: #eef3fa;
        font-size: 32px;
    }
    .pipe-label {
        color: #26364b;
        font-size: 13px;
        line-height: 1.25;
        font-weight: 800;
    }
    .pipe-sub {
        font-size: 11px;
        font-weight: 600;
        color: #5d6b7e;
    }
    .challenge-box {
        border-top: 1px solid #e8edf4;
        padding: 22px 28px 28px;
    }
    .challenge-box h3 {
        color: #1d2d44;
        font-size: 20px;
        margin: 0 0 16px;
        font-weight: 800;
    }
    .challenge-list {
        padding: 0;
        margin: 0;
        list-style: none;
        display: grid;
        gap: 12px;
    }
    .challenge-list li {
        color: #314157;
        font-size: 14px;
        font-weight: 700;
        display: flex;
        gap: 12px;
        align-items: flex-start;
    }
    .challenge-list li:before {
        content: "✓";
        color: #2e6fa9;
        font-weight: 900;
        flex-shrink: 0;
        margin-top: 1px;
    }
    @media (max-width: 900px) {
        .research-layout {
            grid-template-columns: 1fr;
        }
        .research-sidebar {
            display: none;
        }
        .pipeline {
            grid-template-columns: 1fr;
            gap: 18px;
        }
        .pipeline-arrow {
            transform: rotate(90deg);
        }
    }
</style>
""",
        unsafe_allow_html=True,
    )
