from openai import OpenAI
import time

import code.file as file

# Get my API key
parms = file.read_json("parms/openAI.json")

def chat_gpt(prompt):
    client = OpenAI(
        api_key=parms["api_key"],
        )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
