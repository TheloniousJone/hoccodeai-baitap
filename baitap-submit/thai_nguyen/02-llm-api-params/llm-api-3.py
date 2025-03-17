import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import re

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY"),
)

URL = "https://tuoitre.vn/cac-nha-khoa-hoc-nga-bao-tu-manh-nhat-20-nam-sap-do-bo-trai-dat-2024051020334196.htm"
headers = {
    'User-Agent': "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/51.0.2704.64 Safari/537.36"
}
r = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')
content = ""
table = soup.find('div', attrs={'itemprop': 'articleBody'})
for data in table:
    content += re.sub(r'\s+', ' ', data.text).strip()

chat_completion = client.chat.completions.create(
    messages=
    [
        {
            "role": "user",
            "content": f"Dưới đây là nội dung của 1 trang web, hãy giúp tôi tóm tắt nó \n {content}",
        }
    ],
    model="gemma2-9b-it",
    stream=True
)
print('A: ')
for chunk in chat_completion:
    print(chunk.choices[0].delta.content or "", end="")
