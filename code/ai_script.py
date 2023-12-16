import openai

import file

# Get my API key
parms = file.read_json("parms/openAI.json")
# Set your OpenAI API key here
openai.api_key = parms["api_key"]

# The prompt for the AI model
prompt_text = "Once upon a time, there was a dragon"

# Requesting the model to complete the prompt
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt_text,
  max_tokens=50  # Maximum tokens to generate in the completion
)

# Printing the AI-generated completion
print(response.choices[0].text.strip())
