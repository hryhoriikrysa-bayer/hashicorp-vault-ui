import streamlit as st

def config_page():
    st.set_page_config(
        page_icon="static/logo.png",
        page_title="HashiCorp Vault Self Service"
    )

    ICON = "static/fulllogo.png"
    st.logo(ICON, size="large")