import streamlit as st
import json

from openai import OpenAI

st.title("双语单词卡 Bilingual Word Cards")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
password = st.text_input("请输入使用密码", type="password")
if password != st.secrets["APP_PASSWORD"]:
    st.info("输入正确的密码后才能使用")
    st.stop()

rules="""你是幼儿园双语教材编写助手。用户给你一个主题，你给出5个适合5岁孩子的单词。只回复JSON，不要说任何别的话。
主题是中文时，sentence用英文写。例如：
[{"zh":"苹果","en":"apple","sentence":"I like apples."}]
主题是英文时，sentence用中文写。例如：
[{"zh":"苹果","en":"apple","sentence":"我爱吃苹果。"}]"""

topic=st.text_input("想做什么主题的单词卡？What type of cards do you want?")

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