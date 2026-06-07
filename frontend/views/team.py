import streamlit as st
import streamlit.components.v1 as components

TEAM_CARDS = """
    <section class="team-grid">
        <article class="person-card">
            <div class="avatar avatar-a"><div class="avatar-initials">AJ</div></div>
            <h3>Atharv Joshi</h3>
            <div class="person-role">Lead Developer</div>
            <ul class="person-list">
                <li>NLP Pipeline Design</li>
                <li>Backend Development</li>
                <li>Model Integration</li>
            </ul>
        </article>
        <article class="person-card">
            <div class="avatar avatar-d"><div class="avatar-initials">DA</div></div>
            <h3>Drishti Ahuja</h3>
            <div class="person-role">Developer &amp; Researcher</div>
            <ul class="person-list">
                <li>UI/UX Design</li>
                <li>Training, Testing &amp; Evaluation</li>
                <li>Documentation</li>
            </ul>
        </article>
        <article class="person-card">
            <div class="avatar avatar-p"><div class="avatar-initials">AS</div></div>
            <h3>Prof. Abhishek Srivastava</h3>
            <div class="person-role">Academic Guide</div>
            <ul class="person-list">
                <li>Research Guidance</li>
                <li>Project Supervision</li>
                <li>Evaluation &amp; Review</li>
            </ul>
        </article>
    </section>
"""

TEAM_STYLE = """
<style>
    body { margin: 0; font-family: sans-serif; }
    .team-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 20px;
        margin-top: 8px;
    }
    .person-card {
        background: #fff;
        border: 1px solid #dde1e8;
        border-radius: 8px;
        box-shadow: 0 4px 18px rgba(16,33,60,.07);
        padding: 32px 26px 26px;
        text-align: center;
    }
    .avatar {
        width: 110px;
        height: 110px;
        border-radius: 50%;
        margin: 0 auto 16px;
        overflow: hidden;
        background: #d9dce1;
        display: grid;
        place-items: center;
    }
    .avatar-initials {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        display: grid;
        place-items: center;
        color: #fff;
        font-size: 23px;
        font-weight: 800;
    }
    .avatar-a .avatar-initials { background: linear-gradient(160deg, #1f3854, #101b29); }
    .avatar-d .avatar-initials { background: linear-gradient(160deg, #1c1f2c, #a35f57); }
    .avatar-p .avatar-initials { background: linear-gradient(160deg, #2d425b, #131924); }
    .person-card h3 {
        color: #22324b;
        font-size: 16px;
        line-height: 1.2;
        margin: 0 0 4px;
        font-weight: 800;
    }
    .person-role {
        color: #1a73e8;
        font-size: 12px;
        line-height: 1.2;
        margin-bottom: 16px;
        font-weight: 800;
    }
    .person-list {
        display: inline-block;
        margin: 0;
        padding-left: 16px;
        color: #2e3d52;
        font-size: 13px;
        font-weight: 700;
        line-height: 1.7;
        text-align: left;
    }
    @media (max-width: 850px) {
        .team-grid { grid-template-columns: 1fr; }
    }
</style>
"""

TEAM_HTML = "<main style='padding: 16px;'>" + TEAM_CARDS + "</main>" + TEAM_STYLE

def render_team_view():
    components.html(TEAM_HTML, height=400, scrolling=False)