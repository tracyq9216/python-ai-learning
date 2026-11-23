import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Streaming Demo")

topic = st.text_input("Story topic")

def get_text(stream):
    for event in stream:
        if event.type == "response.output_text.delta":
            yield event.delta

if st.button("Tell a story"):
    stream = client.responses.create(
        model="gpt-6-luna",
        input=f"Tell a short story about {topic} in 5 sentences.",
        stream=True,
    )
    st.write_stream(get_text(stream))