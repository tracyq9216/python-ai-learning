from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client=OpenAI()

rules="你是一位幼儿园老师。回答对象是8岁的孩子。每次只说一句话，不超过30个字，用孩子听得懂的词。先说中文，再说一句对应的简单英文。最后根据这个内容再出一个问题考考小朋友是否理解。"

while True:
    question=input("你想问什么？")
    if question=="退出":
        print("下次再见！")
        break
    response=client.responses.create(
        model="gpt-6-luna",
        instructions=rules,
        input=question,
    )

    print(response.output_text)