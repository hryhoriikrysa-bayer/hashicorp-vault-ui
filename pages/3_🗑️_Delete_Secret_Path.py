import streamlit as st

delete_path = st.form("delete_path")

# Input box to provide application name
application = delete_path.text_input("Enter Application Name")

# Input box to provide environment name
env = delete_path.text_input("Enter Environment Name")

# Input box to provide ...
sub = delete_path.text_input("Enter Subcomponent Name")

# Submit button
submit = delete_path.form_submit_button("Delete path")