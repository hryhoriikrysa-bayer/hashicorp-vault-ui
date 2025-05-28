import streamlit as st

new_path = st.form("create_new_path")

# Input box to provide application name
application = new_path.text_input("Application name")

# Input box to provide environment name
env = new_path.text_input("Environment name")

# Input box to provide ...
add = new_path.text_input("Add text")

# Submit button
submit = new_path.form_submit_button("Create new path")