import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Trumpet Scales", page_icon="🎺", layout="wide")

# Streamlit adds its own padding/margins around embedded components — strip those
# so the app fills the page cleanly, and hide the default Streamlit chrome.
st.markdown(
    """
    <style>
        .block-container { padding-top: 1rem; padding-bottom: 0; }
        #MainMenu, header, footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

app_html = Path(__file__).parent.joinpath("index.html").read_text(encoding="utf-8")
components.html(app_html, height=1100, scrolling=True)
