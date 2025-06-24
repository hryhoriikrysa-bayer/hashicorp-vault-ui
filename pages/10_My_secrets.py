import streamlit as st
import streamlit.components.v1 as components

from components.header_components import sidebar_buttons
from components.optional.my_secrets_page.page_render import render_my_secrets_component, render_my_secrets_header

st.set_page_config(
    layout="wide",
    page_icon="static/logo.png",
    page_title="HashiCorp Vault Self Service"
)

ICON = "static/fulllogo.png"
st.logo(ICON, size="large")

data = {
    "Application A": {
        "Environment A1": ["Subcomponent A1.1", "Subcomponent A1.2"],
        "Environment A2": ["Subcomponent A2.1"],
        "Environment A3": ["Subcomponent A2.1"],
        "Environment A4": ["Subcomponent A2.1"]
    },
    "Application B": {
        "Environment B1": ["Subcomponent B1.1"]
    },
    "Application C": {},
    "Application D": {}
}

render_my_secrets_header()
render_my_secrets_component(data)


with st.sidebar:
    components.html(sidebar_buttons, scrolling=True)