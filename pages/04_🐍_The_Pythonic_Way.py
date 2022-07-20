import os
from pathlib import Path

import streamlit as st


def read_markdown(path: str):
    return Path(path).read_text()


def app():
    st.set_page_config(page_title="The Pythonic Way", page_icon="🐍")
    main_markdown_path = os.path.join("assets", "markdown")
    markdown = read_markdown(os.path.join(main_markdown_path, "04_🐍_The_Pythonic_Way.md"))
    st.markdown(markdown, unsafe_allow_html=True)


if __name__ == "__main__":
    app()
