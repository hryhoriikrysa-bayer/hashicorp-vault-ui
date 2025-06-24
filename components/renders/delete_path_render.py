import streamlit.components.v1 as components

from components.header_components import render_header
from components.form_template import get_submit_form
from components.scripts import config_head, validate_form_script


def render_delete_path_header():
    title = "Delete path"
    description = "Delete an existing secret path with form provided below."

    return render_header(title, description)


def render_delete_path_component():
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
     {config_head}
    </head>
    <body>
    <div class = 'px-40'>
        {get_submit_form()}
    </div>
    <script>
        {validate_form_script}
    </script>
    </body>
    </html>
    """

    return components.html(full_html, height=700, scrolling=True)