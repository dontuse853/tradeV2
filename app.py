from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Paper Tape", page_icon="📈", layout="wide", initial_sidebar_state="collapsed")

# Remove Streamlit's header, footer and padding so the simulator fills the page.
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], footer, #MainMenu {display: none;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

PAGE = Path(__file__).parent / "papertape.html"
HEIGHT = 900  # pixels; raise it on a taller screen. The page scrolls inside the frame on small screens.

if hasattr(st, "iframe"):  # newer Streamlit
    st.iframe(PAGE, width="stretch", height=HEIGHT)
else:  # older Streamlit
    import streamlit.components.v1 as components

    components.html(PAGE.read_text(encoding="utf-8"), height=HEIGHT, scrolling=True)
