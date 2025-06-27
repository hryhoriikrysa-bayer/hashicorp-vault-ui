import streamlit.components.v1 as components

from components.config_head import config_head
from components.custom_styles.custom_generics import *


def get_page_title(title):
    html = f"""
      <div class="px-2 {text0_color}">
        <h1 class="text-6xl font-bold">{title}</h1>
      </div>
      """.format(title=title)

    return html

def get_page_description(description):
    html = f"""
      <div class="px-2 {text1_color}">
        <p>{description}</p>
      </div>
      """.format(title=description)

    return html

def get_login_warning(description):
    html = f"""
      <div class="px-2 {text_violet}">
        <p class="text-2xl font-bold">{description}</p>
      </div>
      """.format(title=description)

    return html

def render_header(title=None, description=None, height=150):
    title = get_page_title(title)
    description = get_page_description(description)

    full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
         {config_head}
        </head>
        <body>
            <div>
                <div class = 'space-y-8'>
                    {title}
                    {description}
                    <hr class="border-zinc-600">
                </div>
            </div>
        </body>
        </html>
        """

    return components.html(full_html, height=height)
