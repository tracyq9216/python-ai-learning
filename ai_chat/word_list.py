import streamlit as st

st.title("My Word List")

if "words" not in st.session_state:
    st.session_state["words"]=[]

with st.form("add_word",clear_on_submit=True):
    word=st.text_input("Type a word")
    submitted=st.form_submit_button("Save")

if submitted and word:
    st.session_state["words"].append(word)

st.subheader("Saved words")
for w in st.session_state["words"]:
    st.write(w)