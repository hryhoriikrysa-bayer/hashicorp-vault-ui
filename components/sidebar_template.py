import streamlit as st

def render_sidebar_btns(is_user_logged=False):
    with st.sidebar:
        if is_user_logged:
            st.button("Log me out", use_container_width=True)
        else:
            st.button("Log in", use_container_width=True)