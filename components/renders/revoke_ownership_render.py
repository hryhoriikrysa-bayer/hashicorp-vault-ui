import streamlit.components.v1 as components

from components.header_components import render_header
from components.form_template import get_submit_form
from components.scripts import config_head, validate_form_script


def render_revoke_ownership_header():
    title = "Revoke ownership"
    description = "Revoke ownership of the secret path from specific user with form provided below."

    return render_header(title, description)


def render_revoke_ownership_component():
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
     {config_head}
    </head>
    <body>
    <div class = 'px-40'>
        {get_submit_form(include_owner_input=True)}
    </div>
    <script>
        {validate_form_script}
    </script>
    </body>
    </html>
    """

    return components.html(full_html, height=800, scrolling=True)