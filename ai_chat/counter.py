import streamlit as st

st.title("Counter")

if "count" not in st.session_state:
    st.session_state["count"]=0

if st.button("Add 1"):
    st.session_state["count"]=st.session_state["count"]+1

st.write("Current number:",st.session_state["count"])