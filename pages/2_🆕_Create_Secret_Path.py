import streamlit as st

new_path = st.form("create_new_path")

# Input box to provide application name
application = new_path.text_input("Enter Application Name")

# Input box to provide environment name
env = new_path.text_input("Enter Environment Name")

# Input box to provide ...
sub = new_path.text_input("Enter Subcomponent Name")

# Submit button
submit = new_path.form_submit_button("Create new path")