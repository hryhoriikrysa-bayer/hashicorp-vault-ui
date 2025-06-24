import streamlit.components.v1 as components

from components.custom_styles.custom_list import list_arrow_color, list_text_color
from components.header_components import render_header
from components.scripts import config_head


def render_home_header():
    title = "HashiCorp Vault"
    description = "Self service app. Manage your Hashicorp Vault secrets path."

    return render_header(title, description)


def render_home_component():
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
     {config_head}
    </head>
    <body>
    <div class = 'px-40'>
        <ul class = "list-none space-y-2 px-5">
            <li 
                class="relative pl-6 text-lg {list_text_color} before:content-['➤'] before:absolute before:left-0 before:{list_arrow_color} before:font-bold">
                Create secret paths
            </li>
            <li 
                class="relative pl-6 text-lg {list_text_color} before:content-['➤'] before:absolute before:left-0 before:{list_arrow_color} before:font-bold">
                Delete secret paths
            </li>
            <li 
                class="relative pl-6 text-lg {list_text_color} before:content-['➤'] before:absolute before:left-0 before:{list_arrow_color} before:font-bold">
                Grant ownership of secret path to users
            </li>
            <li 
                class="relative pl-6 text-lg {list_text_color} before:content-['➤'] before:absolute before:left-0 before:{list_arrow_color} before:font-bold">
                Revoke ownership of secret path from users
            </li>
        </ul>
    </div>
    <script>

    </script>
    </body>
    </html>
    """

    return components.html(full_html, height=500, scrolling=True)