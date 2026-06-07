import streamlit as st
import streamlit.components.v1 as components

from views.team import TEAM_CARDS, TEAM_STYLE


def render_contact_view():
    html = (
        "<main style='padding: 16px;'>"
        "<h1 class='page-title'>Contact</h1>"
        "<p class='page-subtitle'>Get in touch with the SupportAI team.</p>"
        + TEAM_CARDS
        + "</main>"
        + TEAM_STYLE
    )
    components.html(html, height=600, scrolling=False)