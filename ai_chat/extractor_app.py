import streamlit as st
import json
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

rules = """You are a meeting notes assistant. Find every to-do item in the notes.
If the owner or deadline is not written, use "Not mentioned".
Write each field in the same language as the notes.
Reply with JSON only, no other words. Format:
[{"owner": "Ms. Wang", "task": "Hand in the midterm exam", "deadline": "Before next Wednesday"}]"""

st.title("Meeting Notes → To-Do List")

if "records" not in st.session_state:
    st.session_state["records"]=[]

with st.form("add_note",clear_on_submit=False):
    note=st.text_area("Type meeting note")
    submitted=st.form_submit_button("Extract")

if submitted and note:
    response=client.responses.create(
        model="gpt-6-luna",
        instructions=rules,
        input=note
    )

    try:
        records=json.loads(response.output_text)

    except json.decoder.JSONDecodeError:
        st.error("AI didn't reply,please try again.")

    else:
        if records==[]:
            st.info("No to-do items found.")
            st.session_state["records"]=[]
        else:
            st.session_state["records"]=records

if st.session_state["records"]:
    st.dataframe(st.session_state["records"])
    st.download_button("Download JSON",json.dumps(st.session_state["records"],ensure_ascii=False),"to-do.json")