import streamlit as st

from components.login_warning_component import render_login_warning_component


def render_form(is_user_logged=False, include_owner_input=False):
    if is_user_logged:
        with st.form("submit_form"):
            app = st.text_input("Application")
            env = st.text_input("Environment")
            subcomp = st.text_input("Subcomponent")

            if include_owner_input:
                owner = st.text_input("Owner")

            submit_btn = st.form_submit_button("Submit", type="primary")
    else:
        render_login_warning_component()

