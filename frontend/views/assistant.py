import streamlit as st


def render_assistant_view():
    st.markdown(
        """
<main class="page-pad assistant-page">
    <h1 class="page-title">AI Assistant</h1>
    <p class="page-subtitle">Generate intelligent responses for customer queries.</p>
</main>
<style>
    .assistant-page + div {
        padding-left: 0;
    }
    .assistant-grid {
        display: grid;
        grid-template-columns: minmax(320px, .95fr) minmax(360px, 1fr);
        gap: 32px;
        padding: 0 44px 48px;
    }
    .panel {
        background: #fff;
        border: 1px solid var(--line);
        border-radius: 8px;
        box-shadow: 0 4px 18px rgba(16,33,60,.07);
        overflow: hidden;
    }
    .panel-body {
        padding: 26px 28px;
    }
    .field-title, .response-label {
        color: #24324a;
        font-size: 15px;
        font-weight: 800;
        margin-bottom: 16px;
    }
    .counter {
        color: #6b7788;
        font-size: 12px;
        margin-top: 6px;
    }
    .tip {
        margin-top: 28px;
        color: #40526a;
        font-size: 14px;
        font-weight: 600;
        line-height: 1.5;
        background: #f1f7ff;
        border: 1px solid #d8e8fb;
        border-radius: 8px;
        padding: 18px 20px;
    }
    .response-row {
        min-height: 72px;
        padding: 18px 28px;
        border-top: 1px solid var(--line);
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: #24324a;
        font-size: 15px;
        font-weight: 800;
    }
    .response-row:first-child {
        border-top: 0;
    }
    .pill {
        border-radius: 999px;
        padding: 7px 14px;
        font-size: 13px;
        font-weight: 800;
    }
    .negative {
        color: #c44a54;
        background: #fdecee;
    }
    .retrieval {
        color: #3972bd;
        background: #e8f1fd;
    }
    .confidence {
        color: #4a9d62;
        background: #e9f7ee;
    }
    .reply-box {
        margin-top: 12px;
        background: #eaf8ee;
        border: 1px solid #ccebd5;
        color: #2e4836;
        border-radius: 8px;
        padding: 18px 20px;
        line-height: 1.55;
        font-size: 14px;
        font-weight: 600;
    }
    .retrieved {
        margin-top: 16px;
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 14px 18px;
        color: #34445b;
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        font-weight: 800;
        cursor: pointer;
    }
    .retrieved-context {
        display: block;
        margin-top: 10px;
        padding: 14px;
        background: #f8fafc;
        border: 1px solid var(--line);
        border-radius: 8px;
        font-size: 13px;
        color: #334156;
        line-height: 1.6;
    }
    @media (max-width: 860px) {
        .assistant-grid {
            grid-template-columns: 1fr;
            padding: 0 20px 32px;
        }
    }
</style>
""",
        unsafe_allow_html=True,
    )

    st.markdown('<section class="assistant-grid"><div>', unsafe_allow_html=True)
    st.markdown('<div class="panel"><div class="panel-body"><div class="field-title">Your Message</div>', unsafe_allow_html=True)
    query = st.text_area(
        "Your Message",
        height=210,
        placeholder="Type or paste the customer message here...",
        max_chars=1000,
        label_visibility="collapsed",
    )
    st.markdown(f'<div class="counter">{len(query)}/1000</div>', unsafe_allow_html=True)
    st.button("Generate Response   →", use_container_width=True)
    st.markdown('</div></div><div class="tip"><b>Tip:</b> Provide as much context as possible for better results.</div></div>', unsafe_allow_html=True)

    st.markdown(
        """
<div class="panel">
    <div class="response-row" style="border-top:0; font-size:16px;"><span>Response</span></div>
    <div class="response-row"><span>Sentiment</span><span class="pill negative">Negative</span></div>
    <div class="response-row"><span>Technique Used</span><span class="pill retrieval">Retrieval-Based</span></div>
    <div class="response-row"><span>Confidence Score</span><span class="pill confidence">0.86</span></div>
    <div class="panel-body">
        <div class="response-label">Generated Reply</div>
        <div class="reply-box">We're sorry to hear about the delay in your order. Please allow us some more time to deliver it to you. You will receive a confirmation email with tracking details shortly.</div>
        <div class="retrieved"><span>View Retrieved Context</span><span>⌄</span></div>
    </div>
</div></section>
""",
        unsafe_allow_html=True,
    )
