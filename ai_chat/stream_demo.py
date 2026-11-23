from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
client=OpenAI()

stream=client.responses.create(
    model="gpt-6-luna",
    input="Tell a short story about a cat in 5 sentences.",
    stream=True,
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta,end="",flush=True)

print()