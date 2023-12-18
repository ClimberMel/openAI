from openai import OpenAI
import time

import code.file as file


# Get my API key
parms = file.read_json("parms/test_openAI.json")

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=parms["api_key"],
    )

def chat_gpt(prompt):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
#        print(response['choices'][0]['message']['content'])

prompt = "What caused the market crash in 1980?"
response = chat_gpt(prompt)

print(response)