import openai
# Set up OpenAI API credentials
from dotenv import dotenv_values, find_dotenv
import os
config = dotenv_values(find_dotenv())
  
openai.api_key = config['openai_api_key']
 
# Function to Rephrase text using OpenAI
def rewrite_text(text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Rephrase with keeping the road names and the city: \"{text}\"",
        max_tokens=50,
        temperature=1
    )
    # print(response)
    rewritten_text = response.choices[0].text.strip()
    return rewritten_text
