import streamlit as st

from components.home_render import render_home_header, render_home_component
from components.page_config import config_page
from components.sidebar_template import render_sidebar_btns

# is_user_logged = st.user.is_logged_in
is_user_logged = True

config_page()

render_sidebar_btns(is_user_logged=is_user_logged)

render_home_header()
render_home_component()

