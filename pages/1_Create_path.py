import streamlit as st
import streamlit.components.v1 as components

from components.renders.create_path_render import render_create_path_header, render_create_path_component
from components.header_components import sidebar_buttons

st.set_page_config(
    layout="wide",
    page_icon="static/logo.png",
    page_title="HashiCorp Vault Self Service"
)

ICON = "static/fulllogo.png"
st.logo(ICON, size="large")

render_create_path_header()
render_create_path_component()

with st.sidebar:
    components.html(sidebar_buttons, scrolling=True)