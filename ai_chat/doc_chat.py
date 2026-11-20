import streamlit as st
from openai import OpenAI 

st.title("Chat With Your Document")

client=OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

summary_rules="""Summarize the document in 3 short bullet points.
Write in the same language as the document."""

uploaded=st.file_uploader("Upload a .txt file",type="txt")

if uploaded:
    text=uploaded.read().decode("utf-8")
    st.write(text)

    if st.button("Summarize"):
        response=client.responses.create(
            model="gpt-6-luna",
            instructions=summary_rules,
            input=text
        )
        st.write(response.output_text)