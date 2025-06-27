import streamlit as st
import streamlit.components.v1 as components

from components.config_head import config_head
from components.html_components import get_login_warning


def render_login_warning():
    description = get_login_warning("In order to access features, you must first log in")

    full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
         {config_head}
        </head>
        <body>
            <div>
                <div class = 'space-y-8'>
                    {description}
                </div>
            </div>
        </body>
        </html>
        """

    return components.html(full_html, height=40)

def render_login_warning_component():
    render_login_warning()

    left, middle, right = st.columns(3)
    if left.button("Log in with x", use_container_width=True):
        left.markdown("login x")
    if middle.button("Login with y", use_container_width=True):
        middle.markdown("login y")
    if right.button("Login with z", use_container_width=True):
        right.markdown("login z")
