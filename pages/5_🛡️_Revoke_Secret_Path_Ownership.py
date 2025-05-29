import streamlit as st

revoke = st.form("revoke_secret")

# Input box to provide application name
application = revoke.text_input("Enter Application Name")

# Input box to provide environment name
env = revoke.text_input("Enter Environment Name")

# Input box to provide ...
sub = revoke.text_input("Enter Subcomponent Name")

# Submit button
submit = revoke.form_submit_button("Revoke secret path ownership")