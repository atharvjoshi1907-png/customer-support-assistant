import streamlit as st
import plotly.graph_objects as go

def render_accuracy_chart():
    # Production dummy accuracy telemetry metrics
    epochs = [1, 2, 3, 4]
    accuracy = [76.5, 84.2, 89.8, 94.2]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=epochs, 
        y=accuracy, 
        mode='lines+markers',
        line=dict(color='#38bdf8', width=3),
        marker=dict(size=8, color='#818cf8'),
        name='Accuracy Curve'
    ))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  # Deep transparent background flush
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#f8fafc', family='sans-serif'),
        margin=dict(l=40, r=20, t=20, b=40),
        height=300,
        xaxis=dict(
            title="Training Checkpoints",
            gridcolor='rgba(255, 255, 255, 0.05)',
            zeroline=False,
            showgrid=True
        ),
        yaxis=dict(
            title="Accuracy Score (%)",
            gridcolor='rgba(255, 255, 255, 0.05)',
            zeroline=False,
            showgrid=True
        )
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})


def render_latency_chart():
    # Production dummy response timeline parameters
    batch = ["Batch A", "Batch B", "Batch C", "Batch D"]
    latency = [0.45, 0.38, 0.29, 0.24]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=batch, 
        y=latency,
        marker_color='rgba(56, 189, 248, 0.7)',
        marker_line=dict(color='#38bdf8', width=1.5),
        name='Inference Delay'
    ))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  # Deep transparent background flush
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#f8fafc', family='sans-serif'),
        margin=dict(l=40, r=20, t=20, b=40),
        height=300,
        xaxis=dict(
            gridcolor='rgba(255, 255, 255, 0.05)',
            showgrid=False
        ),
        yaxis=dict(
            title="Latency Metrics (s)",
            gridcolor='rgba(255, 255, 255, 0.05)',
            zeroline=False,
            showgrid=True
        )
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})