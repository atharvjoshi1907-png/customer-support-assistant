import streamlit as st
from components.footer import render_footer

def render_contact_view():
    st.markdown("<h2 style='font-weight: 800; margin-bottom: 25px; letter-spacing: -0.5px;'>Get in Touch with Us</h2>", unsafe_allow_html=True)

    left, right = st.columns([1, 1.4])
    with left:
        st.markdown("""
            <div style="padding: 24px; border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.15); background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(8px); color: #ffffff;">
                <p style='margin: 8px 0; font-size: 16px;'><b>Our Workspace Hub</b><br><span style='opacity: 0.7;'>IIT Indore Lab Campus, MP, India</span></p>
                <p style='margin: 8px 0; font-size: 16px;'><b>Project Inquiry Channels</b><br><span style='color: #38bdf8;'>supportai@iiti.ac.in</span></p>
            </div>
        """, unsafe_allow_html=True)

    with right:
        st.text_input("Your Full Name")
        st.text_input("Your Email Address")
        st.text_area("Write Your Message Here", height=120)
        st.button("Send Message", type="primary")

    render_footer()