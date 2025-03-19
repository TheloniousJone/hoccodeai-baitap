import os
from openai import OpenAI
import re

def send_request(input_text):
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an expert Python Developer."},
            {"role": "user", "content": input_text}
        ],
        model="gemma2-9b-it"
    )

    return chat_completion.choices[0].message.content


input_question = input('Input the python exercise: ')
output = send_request(input_question)
code_match = re.findall(r"```python(.*?)```", output, re.DOTALL)
if code_match:
    python_code = code_match[0].strip()
    print("Extracted Code:\n", python_code)
    with open("final.py", "w") as output_file:
        # clear the output file
        output_file.truncate(0)
        output_file.write(python_code)
else:
    print("No code found in the response.")

