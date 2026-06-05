import streamlit as st

from views.team import TEAM_CARDS, TEAM_STYLE


def render_contact_view():
    st.markdown(
        f"""
<main class="page-pad">
    <h1 class="page-title">Contact</h1>
    <p class="page-subtitle">Get in touch with the SupportAI team.</p>
    {TEAM_CARDS}
</main>
{TEAM_STYLE}
""",
        unsafe_allow_html=True,
    )
