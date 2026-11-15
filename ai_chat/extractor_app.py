import streamlit as st
import json
from openai import OpenAI
from datetime import date

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

rules = """You are an assistant for a teacher. 
Find every to-do item in school meeting notes or parent messages.
Only include things someone must do. 
Rules and general reminders are not to-do items.
If the owner or deadline is not written, use "Not mentioned".
Also give "due_date": the deadline as a date in YYYY-MM-DD, worked out from today's date.
If there is no deadline, use "".
Write owner, task and deadline in the same language as the notes.
Reply with JSON only, no other words. 
Format:
[{"owner": "Ms. Wang", "task": "Hand in the midterm exam", "deadline": "Before next Wednesday","due_date":"2026-11-18"}]"""

def sort_key(record):
    if record["due_date"]=="":
        return "9999-12-31"
    return record["due_date"]

st.title("Meeting Notes → To-Do List")

if "records" not in st.session_state:
    st.session_state["records"]=[]

with st.form("add_note",clear_on_submit=False):
    note=st.text_area("Type meeting note")
    submitted=st.form_submit_button("Extract")

if submitted and note:
    response=client.responses.create(
        model="gpt-6-luna",
        instructions=rules+"\nToday is "+str(date.today()),
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
            records=sorted(records,key=sort_key)
            st.session_state["records"]=records

if st.session_state["records"]:
    st.dataframe(st.session_state["records"])
    st.download_button("Download JSON",json.dumps(st.session_state["records"],ensure_ascii=False),"to-do.json")