import streamlit as st
import streamlit.components.v1 as components

from components.header_components import sidebar_buttons
from components.renders.revoke_ownership_render import render_revoke_ownership_header, render_revoke_ownership_component

st.set_page_config(
    layout="wide",
    page_icon="static/logo.png",
    page_title="HashiCorp Vault Self Service"
)

ICON = "static/fulllogo.png"
st.logo(ICON, size="large")

render_revoke_ownership_header()
render_revoke_ownership_component()

with st.sidebar:
    components.html(sidebar_buttons, scrolling=True)