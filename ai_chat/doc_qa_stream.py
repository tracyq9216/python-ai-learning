import streamlit as st
from openai import OpenAI

st.title("Ask Your Document")

uploaded=st.file_uploader("Upload a .txt file",type="txt")
if not uploaded:
    st.info("Upload a .txt file to start.")
    st.stop()
text=uploaded.getvalue().decode("utf-8")

doc_rules="""Answer questions using only the document below.
If the answer is not in the document, say you cannot find it in the document.
Answer in the same language as the question.

Document:
"""+text

client=OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_text(stream):
    for event in stream:
        if event.type == "response.output_text.delta":
            yield event.delta

if "messages" not in st.session_state:
    st.session_state["messages"]=[]

for m in st.session_state["messages"]:
    with st.chat_message(m["role"]):
        st.write(m["content"])

question=st.chat_input("Ask a question")

if question:
    st.session_state["messages"].append({"role":"user","content":question})
    stream=client.responses.create(
        model="gpt-6-luna",
        instructions=doc_rules,
        input=st.session_state["messages"],
        stream=True,
    )
    with st.chat_message("user"):
        st.write(question)
    with st.chat_message("assistant"):
        answer=st.write_stream(get_text(stream))  
    st.session_state["messages"].append({"role":"assistant","content":answer})
    st.rerun()