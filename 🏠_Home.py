import os

import streamlit as st
from PIL import Image


def app():
    st.set_page_config(page_title="Home", page_icon="🏠")
    st.subheader("Introduction to Python 🐍: Basics for Engineering ⚙️")
    st.markdown("**_A simple workshop module introducing Python basics for engineering._**")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("Brought to you by [**Engineer Connect**](https://www.linkedin.com/company/engineerconnect/) in collaboration with [**PT. Jokeen Solusi Teknologi (Jokeen.id)**](https://www.linkedin.com/company/jokeen-id/)")

    jokeen_logo = Image.open(os.path.join("static", "jokeen_logo.png"))
    engineer_connect_logo = Image.open(os.path.join("static", "ec_logo.png"))
    adit_circ = Image.open(os.path.join("static", "adit_circ.png"))

    c1,c2,_,_,_ = st.columns(5)
    c1.image(engineer_connect_logo)
    c2.image(jokeen_logo)
    st.markdown("Made & taught with ❤️ by [Aditya Wardianto](https://www.linkedin.com/in/adityawardianto/)")
    c3,_,_,_,_ = st.columns(5)
    c3.image(adit_circ)

if __name__=="__main__":
    app()