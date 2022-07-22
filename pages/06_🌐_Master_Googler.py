import os
import re
from pathlib import Path

import streamlit as st


def read_markdown(path: str):
    return Path(path).read_text()


def app():
    st.set_page_config(page_title="Master Googler", page_icon="🌐")
    main_markdown_path = os.path.join("assets", "markdown")
    markdown = read_markdown(os.path.join(main_markdown_path, "06_🌐_Master_Googler.md"))
    list_of_image = re.findall(r"\!\[image\]\((.*)\)", markdown)
    list_of_source = re.findall(r"source:(.*)", markdown)
    markdown_chunks = re.split(r"[ ?]*\!\[image\]\(.*\)\n[ ?]*source:.*", markdown)

    st.markdown(markdown_chunks[0], unsafe_allow_html=True)
    # st.markdown(markdown, unsafe_allow_html=True)
    for md, im, sc in zip(markdown_chunks[1:], list_of_image, list_of_source):
        st.image(im, use_column_width=True, caption=sc)
        st.markdown(md, unsafe_allow_html=True)


if __name__ == "__main__":
    app()
