# mistral_endpoint.py
import os
from dotenv import load_dotenv
load_dotenv()

from mistralai import Mistral

api_key = os.environ.get('MISTRAL_API_KEY')
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def mistral_endpoint(prompt: str):
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )
    return chat_response.choices[0].message.content
