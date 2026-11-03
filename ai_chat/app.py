import streamlit as st
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client=OpenAI()

st.title("双语单词卡")

rules="""你是幼儿园双语教材编写助手。用户给你一个主题，你给出5个适合5岁孩子的单词。只回复JSON，不要说任何别的话。格式如下：
[
  {"zh":"苹果","en":"apple","sentence":"I like apples."}
]"""

topic=st.text_input("想做什么主题的单词卡？")

if st.button("生成"):
    if topic=="":
        st.warning("请先输入一个主题")
    else:
        with st.spinner("正在生成卡片……"):
            response=client.responses.create(
                model="gpt-6-luna",
                instructions=rules,
                input=topic,
            )

            try:
                cards=json.loads(response.output_text)
                
            except json.decoder.JSONDecodeError:
                st.error(f"AI这次没按格式交作业，请再试一次")

            else:
                for card in cards:
                    zh=card["zh"]
                    en=card["en"]
                    sentence=card["sentence"]
                    with st.container(border=True):
                        st.subheader(f"{zh}/{en}")
                        st.write(sentence)
                    
                with open(f"{topic}_cards.json","w",encoding="utf-8")as f:
                    json.dump(cards,f,ensure_ascii=False,indent=2)