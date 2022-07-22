import os

import streamlit as st
from PIL import Image


def app():
    st.set_page_config(page_title="About Us", page_icon="🧑")
    image_path = os.path.join(".", "assets", "image")
    engineer_connect_logo = Image.open(os.path.join(image_path, "ec_logo.png"))
    jokeen_logo = Image.open(os.path.join(image_path, "jokeen_logo.png"))
    adit_circ = Image.open(os.path.join(image_path, "adit_circ.png"))

    about_eng_con(engineer_connect_logo)

    about_jokeen(jokeen_logo)

    about_speaker(adit_circ)


def about_speaker(adit_circ):
    st.markdown("## About Speaker")
    c1, c2 = st.columns([1, 4])
    c1.image(adit_circ)
    c2.markdown(
        """
    - Aditya Wardianto or Adit is a Final Year undergraduate student from Biomedical Engineering Department Sepuluh Nopember Institute of Technology.\n
    - He has used Python for 3+ years to freelance and is currently freelancing as a machine learning engineer at PT Jokeen Solusi Teknologi.\n
    - He is a Certified Tensorflow Developer thanks to Bangkit Academy led by Google, GoTo, and Traveloka.
    """
    )


def about_jokeen(jokeen_logo):
    st.markdown("## About Jokeen.id")
    st.video(r"https://www.youtube.com/watch?v=SxkT0awrfFc")
    c1, c2 = st.columns([1, 4])
    c1.image(jokeen_logo)
    c2.markdown(
        """
        - Jokeen.id is a start-up in the field of engineering that was established on February 7, 2020.\n
        - Jokeen.id provides services ranging from and not restricted to mechanical product development, engineering design work, manufacture, to mass production of mechatronic products.\n
        - In our work, we uphold client satisfaction by prioritizing professionalism and punctuality.\n
        - Contact Us through [WA]("https://wa.me/6281357172537") - [Linkedin]("https://www.linkedin.com/company/jokeen-id/") - [Instagram](https://www.instagram.com/jokeen.id/) 
        """
    )


def about_eng_con(engineer_connect_logo):
    st.markdown("""## About Engineer Connect""")
    c1, c2 = st.columns([1, 4])
    c1.image(engineer_connect_logo)
    c2.markdown(
        """
        - Engineer Connect is a platform to connect Indonesia's engineering students, where they can study together, fulfill their academic needs, and share their engineering knowledge.\n
        - Engineer Connect's services range from Engineer Group Study, Skill Workshop, and On-Demand Tutor.\n
        - Engineer Connect is also supported and part of the Leadership Project of Young Leaders of Indonesia by McKinsey & Company.\n
        - Engineer Connect will always strive to provide the best service quality and effectively connect Indonesia's engineering students.
        """
    )


if __name__ == "__main__":
    app()
