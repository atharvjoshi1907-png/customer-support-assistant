import pandas as pd
import plotly.express as px
import streamlit as st


def _bar_chart(data, x, y, color):
    fig = px.bar(data, x=x, y=y, text=y)
    fig.update_traces(
        marker_color=color,
        textposition="outside",
        textfont=dict(size=13, color="#2f78d6", family="Inter"),
        cliponaxis=False,
    )
    fig.update_layout(
        height=236,
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        showlegend=False,
        xaxis=dict(title="", tickfont=dict(size=12, color="#5d6b7e"), showgrid=False),
        yaxis=dict(title="", tickfont=dict(size=12, color="#8a97a8"), gridcolor="#eef2f7", zeroline=False),
        bargap=.58,
        font=dict(family="Inter"),
    )
    return fig


def render_analytics_view():
    st.markdown(
        """
<main class="page-pad analytics-page">
    <h1 class="page-title">Analytics Dashboard</h1>
    <p class="page-subtitle">Performance overview of implemented models.</p>
    <section class="metric-grid">
        <div class="metric-card"><div><div class="metric-val">88%</div><div class="metric-lbl">Accuracy<br>(Highest)</div></div><div class="metric-icon">📈</div></div>
        <div class="metric-card"><div><div class="metric-val">0.4s</div><div class="metric-lbl">Avg. Latency<br>(Seconds)</div></div><div class="metric-icon">⏱</div></div>
        <div class="metric-card"><div><div class="metric-val">100%</div><div class="metric-lbl">Validation Score<br>(Passing)</div></div><div class="metric-icon">✅</div></div>
        <div class="metric-card"><div><div class="metric-val">500+</div><div class="metric-lbl">Training Samples<br>(Processed)</div></div><div class="metric-icon">🗄️</div></div>
    </section>
</main>
<style>
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 22px;
        margin-bottom: 28px;
    }
    .metric-card {
        min-height: 112px;
        background: #fff;
        border: 1px solid #e8edf4;
        border-radius: 8px;
        box-shadow: 0 4px 18px rgba(16,33,60,.07);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 20px 24px;
    }
    .metric-val {
        color: #2f78d6;
        font-size: 30px;
        line-height: 1;
        font-weight: 800;
        margin-bottom: 8px;
    }
    .metric-lbl {
        color: #24324a;
        font-size: 12px;
        font-weight: 800;
        line-height: 1.4;
    }
    .metric-icon {
        width: 52px;
        height: 52px;
        border-radius: 50%;
        display: grid;
        place-items: center;
        font-size: 22px;
        background: #eef5ff;
        flex-shrink: 0;
    }
    .chart-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 22px;
        padding: 0 44px 22px;
    }
    .chart-card, .summary-card {
        background: #fff;
        border: 1px solid #e8edf4;
        border-radius: 8px;
        box-shadow: 0 4px 18px rgba(16,33,60,.07);
        padding: 22px 24px;
    }
    .chart-title, .summary-title {
        color: #24324a;
        font-size: 15px;
        font-weight: 800;
        margin-bottom: 16px;
    }
    .summary-card {
        margin: 0 44px 44px;
    }
    .summary-card p {
        color: #2e3e55;
        font-size: 15px;
        font-weight: 600;
        line-height: 1.6;
        margin: 0;
    }
    @media (max-width: 900px) {
        .metric-grid, .chart-grid {
            grid-template-columns: 1fr;
        }
        .chart-grid {
            padding: 0 20px 22px;
        }
        .summary-card {
            margin: 0 20px 32px;
        }
    }
</style>
""",
        unsafe_allow_html=True,
    )

    acc_data = pd.DataFrame({"Model": ["Baseline", "Rule-Based", "Retrieval-Based"], "Accuracy": [72, 80, 88]})
    lat_data = pd.DataFrame({"Model": ["Baseline", "Rule-Based", "Retrieval-Based"], "Latency": [2.5, 0.1, 0.4]})

    st.markdown('<section class="chart-grid"><div class="chart-card"><div class="chart-title">Accuracy Comparison (%)</div>', unsafe_allow_html=True)
    st.plotly_chart(_bar_chart(acc_data, "Model", "Accuracy", "#2f78d6"), use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div><div class="chart-card"><div class="chart-title">Latency Comparison (Seconds)</div>', unsafe_allow_html=True)
    st.plotly_chart(_bar_chart(lat_data, "Model", "Latency", "#5b9bd6"), use_container_width=True, config={"displayModeBar": False})
    st.markdown(
        """
</div></section>
<section class="summary-card">
    <div class="summary-title">Model Performance Summary</div>
    <p>Retrieval-Based approach achieves the best balance between accuracy and latency.<br>It leverages contextual information to generate more relevant responses.</p>
</section>
""",
        unsafe_allow_html=True,
    )
