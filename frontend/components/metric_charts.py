import streamlit as st
import plotly.graph_objects as go

def render_accuracy_chart():
    epochs = [1, 2, 3, 4]
    accuracy = [76.5, 84.2, 89.8, 94.2]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=epochs, y=accuracy, mode='lines+markers',
        line=dict(color='#38bdf8', width=4),
        marker=dict(size=10, color='#818cf8')
    ))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#ffffff', family='sans-serif', size=15), # Increased font base scale
        margin=dict(l=50, r=20, t=20, b=50),
        height=320,
        xaxis=dict(title="Training Steps", gridcolor='rgba(255, 255, 255, 0.08)', tickfont=dict(size=14)),
        yaxis=dict(title="Accuracy (%)", gridcolor='rgba(255, 255, 255, 0.08)', tickfont=dict(size=14))
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def render_latency_chart():
    batch = ["Batch A", "Batch B", "Batch C", "Batch D"]
    latency = [0.45, 0.38, 0.29, 0.24]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=batch, y=latency, marker_color='rgba(56, 189, 248, 0.85)'))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#ffffff', family='sans-serif', size=15),
        margin=dict(l=50, r=20, t=20, b=50),
        height=320,
        xaxis=dict(tickfont=dict(size=14)),
        yaxis=dict(title="Speed (Seconds)", gridcolor='rgba(255, 255, 255, 0.08)', tickfont=dict(size=14))
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})