"""
Configuration utilities for the AI agent application.
Handles environment variables and settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_env_var(key, default=None):
    """
    Get an environment variable value with a fallback default.
    
    Args:
        key (str): The environment variable name
        default: Default value if environment variable is not found
        
    Returns:
        The value of the environment variable or the default
    """
    return os.environ.get(key, default)

# API keys
MISTRAL_API_KEY = get_env_var('MISTRAL_API_KEY')

# Application settings
DEFAULT_MODEL = get_env_var('DEFAULT_MODEL', 'mistral-large-latest')
