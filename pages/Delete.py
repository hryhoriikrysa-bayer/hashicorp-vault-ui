import streamlit as st

delete_path = st.form("delete_path")

# Input box to provide application name
application = delete_path.text_input("Application name")

# Input box to provide environment name
env = delete_path.text_input("Environment name")

# Input box to provide ...
add = delete_path.text_input("Add text")

# Submit button
submit = delete_path.form_submit_button("Delete path")