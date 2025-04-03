import os

from mistralai import Mistral

api_key = os.environ.get('MISTRAL_API_KEY') or 'fYyxtXD3JtccTu6iGz6V2W4I3N3bg8w1'
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def run_mistral(prompt: str):
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

if __name__ == "__main__":
    run_mistral()
