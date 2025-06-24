import streamlit.components.v1 as components

from components.custom_styles.custom_generics import *
from components.optional.custom_styles.custom_mysecrets import *
from components.scripts import config_head

logout_button = f"""
    <button onclick="" class="shrink-0 rounded-full border {logout_button_border_color} {logout_button_bg_color} {logout_button_text_color} px-3 py-1 rounded">
        Logout
    </button>
"""

sidebar_buttons = f"""
   <!DOCTYPE html>
    <html>
    <head>
         {config_head}
    </head>
    <body>
        <div class = 'flex items-center grid grid-cols-1 grid-rows-1 gap-4'>
            {logout_button}
        </div>
    </body>
    </html>
"""

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
        <p class="xl">{description}</p>
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
            <div class = 'px-40'>
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
