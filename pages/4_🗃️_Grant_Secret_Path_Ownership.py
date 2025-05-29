import streamlit as st

grant_path = st.form("grant_secret_path")

# Input box to provide application name
application = grant_path.text_input("Enter Application Name")

# Input box to provide environment name
env = grant_path.text_input("Enter Environment Name")

# Input box to provide ...
sub = grant_path.text_input("Enter Subcomponent Name")

# Submit button
submit = grant_path.form_submit_button("Grant secret path ownership")