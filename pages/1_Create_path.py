import streamlit as st

from components.form_template import render_form
from components.html_components import render_header
from components.page_config import config_page
from components.sidebar_template import render_sidebar_btns

# is_user_logged = st.user.is_logged_in
is_user_logged = True

config_page()

render_sidebar_btns(is_user_logged=is_user_logged)

render_header("Create path", "Create a new secret path with form provided below.")
render_form(is_user_logged=is_user_logged)