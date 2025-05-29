import streamlit as st

st.set_page_config(
    page_title="Vault",
    page_icon="🔒",
    layout="centered"
)

col1, col2, col3 = st.columns([1,4,1])
col2.title("HashiCorp Vault APP")

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

col4, col5, col6 = st.columns([1,20,1])
col5.header("This is the app to store and manage your secrets inside of HashiCorp Vault")