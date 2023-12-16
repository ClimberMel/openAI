import openai
import os
import json

def generate_text(prompt_text):
    # Construct the file path using os.path.join
    file_path = os.path.join('parms', 'openAI.json')

    # Get the API key
    with open(file_path, 'r') as file:
        parms = json.load(file)
    openai.api_key = parms["api_key"]

    # Request the model to complete the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_text,
        max_tokens=50
    )

    # Return the AI-generated completion
    print(response.choices[0].text.strip()) 
    return response.choices[0].text.strip()

# Example usage
# generate_text("Your prompt here")
