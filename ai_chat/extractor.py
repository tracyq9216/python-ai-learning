import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client=OpenAI()

rules="""你是一个会议记录助手，用户给你会议记录，你列出相关的内容。如果记录里没写负责人或截止时间，就填"未提及"。只回复JSON，不要说任何话。格式如下：
[{"owner":"王老师","task":"交期中试卷","deadline":"下周三前"}]"""

content=input("会议内容有哪些？")
response=client.responses.create(
    model="gpt-6-luna",
    instructions=rules,
    input=content
)

try:
    records=json.loads(response.output_text)

except json.decoder.JSONDecodeError:
    print("AI这次没按格式回复，请再试一次")

else:
    if records==[]:
        print("没有找到待办事项")
    for record in records:
        owner=record["owner"]
        task=record["task"]
        deadline=record["deadline"]
        print(f"{owner}/{task}/{deadline}")