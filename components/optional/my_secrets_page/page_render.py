import streamlit.components.v1 as components

from components.header_components import render_header
from components.optional.modal_forms.modals import grant_ownership_modal, delete_item_modal, revoke_ownership_modal
from components.optional.scripts import toggle_hidden_script, toggle_modal_script, go_to_details_script
from components.optional.tree_list.tree_list import generate_tree_list
from components.scripts import config_head


def render_my_secrets_header():
    title = "My Secrets"
    description = "Here are paths for all of your stored secrets. Select desired subcomponent to access it's underlying secrets and keys."

    return render_header(title, description, height=200)


def render_my_secrets_component(data):
    tree_list = generate_tree_list(data)

    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
     {config_head}
    </head>
    <body>
    {grant_ownership_modal}
    {revoke_ownership_modal()}
    {delete_item_modal}
    <div class = 'px-40'>
        <div class="space-y-6 text-base rounded">
            {tree_list}
        </div>
    </div>
    <script>
        {toggle_hidden_script}
        {toggle_modal_script}
        {go_to_details_script}
    </script>
    </body>
    </html>
    """

    return components.html(full_html, height=500, scrolling=True)