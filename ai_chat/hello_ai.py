from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client=OpenAI()
question=input("你想问什么？")
response=client.responses.create(
    model="gpt-6-luna",
    input=question,
)

print(response.output_text)