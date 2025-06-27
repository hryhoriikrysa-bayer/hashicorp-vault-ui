import re
import streamlit as st

from components.login_warning_component import render_login_warning_component

ERRORS = {
    1: "Cannot be empty",
    2: "Can only contain letters and numbers"
}

def validate_input(input):
    if input is None or input == "":
        return 1

    pattern = r'^[\w\s]+$'
    if re.match(pattern, input) is None:
        return 2

    return 0


def render_form(is_user_logged=False, include_owner_input=False):
    if is_user_logged:
        user_data = {}
        user_errors = {}

        with st.form("submit_form"):
            user_data["Application"] = st.text_input("Application")
            user_data["Environment"] = st.text_input("Environment")
            user_data["Subcomponent"] = st.text_input("Subcomponent")

            if include_owner_input:
                user_data["Owner"] = st.text_input("Owner")

            submit_btn = st.form_submit_button("Submit", type="primary")

            if submit_btn:
                for key, value in user_data.items():
                    response = validate_input(value)
                    if response != 0:
                        user_errors[key] = f"Field {key}: {ERRORS[response]}"

                if user_errors:
                    for key in user_errors:
                        st.error(user_errors[key])
                else:
                    st.success("Submitted")

    else:
        render_login_warning_component()

