import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY"),
)

assistant_content = ""
question = input('Q: ')
chat_completion = client.chat.completions.create(
    messages=
    [
        {
            "role": "user",
            "content": question,
        }
    ],
    model="gemma2-9b-it",
    stream=True
)
print('A: ')
for chunk in chat_completion:
    print(chunk.choices[0].delta.content or "", end="")
