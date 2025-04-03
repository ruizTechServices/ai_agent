"""
Mistral AI API integration module.
Provides functions to interact with the Mistral API for AI text generation.
"""

from mistralai import Mistral
from utils.config import MISTRAL_API_KEY, DEFAULT_MODEL

# Initialize Mistral client
client = Mistral(api_key=MISTRAL_API_KEY)

def run_mistral(prompt: str, model: str = None):
    """
    Send a prompt to the Mistral AI API and get a response.
    
    Args:
        prompt (str): The prompt to send to the model
        model (str, optional): The model to use. Defaults to the value in config.py
        
    Returns:
        str: The generated response from Mistral AI
        
    Raises:
        Exception: If the API call fails or the API key is invalid
    """
    # Use the default model from config if none specified
    model = model or DEFAULT_MODEL
    
    if not MISTRAL_API_KEY:
        raise ValueError("MISTRAL_API_KEY not found in environment variables")
    
    # Make the API request
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )
    
    # Extract and return the generated text
    return chat_response.choices[0].message.content


if __name__ == "__main__":
    # Simple test for direct execution
    test_prompt = "Hello, how are you today?"
    try:
        response = run_mistral(test_prompt)
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error calling Mistral API: {e}")
