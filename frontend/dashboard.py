import streamlit as st

st.set_page_config(
    page_title="Customer Support Assistant",
    page_icon="🤖",
    layout="wide"
)

# HERO SECTION
import streamlit as st

st.set_page_config(
    page_title="Customer Support Assistant",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

.hero-container{
    background:
    linear-gradient(
        rgba(0,40,60,0.65),
        rgba(0,120,140,0.55)
    ),
    url("https://www.mckinsey.com/~/media/mckinsey/business%20functions/operations/our%20insights/the%20state%20of%20customer%20care%20in%202022/the%20state%20of%20customer%20care%20in%202022_1132839148_thumb_1536x1536.jpg");

    background-size: cover;
    background-position: center;

    padding: 120px 60px;
    border-radius: 20px;
    text-align:center;
}

.hero-container h1{
    color:white;
    font-size:60px;
    margin-bottom:20px;
}

.hero-container p{
    color:white;
    font-size:22px;
    max-width:900px;
    margin:auto;
    line-height:1.6;
}
</style>

<div class="hero-container">
<h1>Sentiment-Aware Customer Support Assistant</h1>

<p>
Generate professional customer support replies using
fine-tuned language models and compare multiple
fine-tuning techniques side-by-side.
</p>

<br>

<p>
Let's get started. What customer issue are you trying to resolve today?
</p>

</div>
            

            
""", unsafe_allow_html=True)
st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)

# Centered button that visually sits inside the banner
left, center, right = st.columns([3, 2, 3])

with center:
    if st.button("🚀 Open Reply Generator"):
        st.switch_page("pages/01_reply_generator.py")


st.markdown("---")


col_a, col_b = st.columns(2)

with col_a:
    st.markdown("**Fine-tuning techniques**")
    st.markdown(
        "- 🔵 **LoRA** — low-rank adapter matrices\n"
        "- 🟣 **QLoRA** — LoRA on a 4-bit quantised model\n"
        "- 🟠 **Full Fine-Tuning** — all weights updated\n"
        "- 🟡 **Prompt Tuning** — virtual token training only"
    )

with col_b:
    st.markdown("**Evaluation metrics tracked**")
    st.markdown(
        "- 📉 Validation loss & perplexity\n"
        "- 📊 BLEU score vs. reference replies\n"
        "- ⏱️ Training time & peak memory\n"
        "- 🧑‍⚖️ Manual tone & relevance review"
    )

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Fine-tune Techniques", "4", help="LoRA · QLoRA · Full FT · Prompt Tuning")
col2.metric("Base Model", "Qwen2.5-0.5B", help="Small language model used for fine-tuning, https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct")
col3.metric("Backend", "🟢 Online")  #replace with backendstatus() once coded
col4.metric("Phase", "2 / 5")

st.markdown("---")
st.info("👈 Select a page from the sidebar to get started.", icon="ℹ️")