import os
import tiktoken
from openai import OpenAI

MAX_TOKENS = 700  # Context window size

encodings = tiktoken.encoding_for_model("gpt-4o")


def split_script(text, max_tokens=MAX_TOKENS):
    """Splits the script into chunks of max_tokens."""
    tokens = encodings.encode(text)
    chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]
    text_chunks = [encodings.decode(chunk) for chunk in chunks]
    return text_chunks


def send_request(input_text):
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.environ.get("GROQ_API_KEY"),
    )
    chunks = split_script(input_text)
    output = ""
    for chunk in chunks:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an expert translator from Vietnamese to English."},
                {"role": "user", "content": chunk}
            ],
            model="gemma2-9b-it",
            stream=True
        )

        response_text = ""
        for response in chat_completion:
            if hasattr(response, "choices") and response.choices:
                content = response.choices[0].delta.content
                if content:
                    response_text += content
                    print(content, end="", flush=True)  # Print live response
        output += response_text
        print("\n")
    return output


input_file = open("Input.txt").read()
output = send_request(input_file)
with open("Output.txt", "w") as output_file:
    # clear the output file
    output_file.truncate(0)
    output_file.write(output)
