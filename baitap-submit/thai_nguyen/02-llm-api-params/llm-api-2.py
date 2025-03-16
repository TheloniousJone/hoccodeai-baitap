import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY"),
)

assistant_content = ""
question = ""
input_message = []
while question != "exit":
    question = input('Q: ')
    input_message.append({
        "role": "user",
        "content": question
    })

    chat_completion = client.chat.completions.create(
        messages=input_message,
        model="gemma2-9b-it",
        stream=True
    )
    full_answer = ""
    print('A: ')
    for chunk in chat_completion:
        content = chunk.choices[0].delta.content or ""
        print(content, end="")
        full_answer += content

    input_message.append({
        "role": "assistant",
        "content": full_answer
    })
