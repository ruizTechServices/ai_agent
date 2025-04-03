"""
Unit tests for the Mistral AI module.
"""

import unittest
from unittest.mock import patch, MagicMock
from modules.ai.mistral import run_mistral

class TestMistral(unittest.TestCase):
    
    @patch('modules.ai.mistral.client')
    def test_run_mistral(self, mock_client):
        """Test that run_mistral correctly calls the Mistral API and returns the response."""
        # Set up the mock response
        mock_choice = MagicMock()
        mock_choice.message.content = "This is a test response from Mistral AI."
        
        mock_response = MagicMock()
        mock_response.choices = [mock_choice]
        
        mock_client.chat.complete.return_value = mock_response
        
        # Call the function with a test prompt
        test_prompt = "What is the capital of France?"
        response = run_mistral(test_prompt)
        
        # Verify the client was called with the correct parameters
        mock_client.chat.complete.assert_called_once()
        call_args = mock_client.chat.complete.call_args[1]
        
        self.assertEqual(call_args['model'], 'mistral-large-latest')  # Default model
        self.assertEqual(call_args['messages'][0]['role'], 'user')
        self.assertEqual(call_args['messages'][0]['content'], test_prompt)
        
        # Verify the response is correctly returned
        self.assertEqual(response, "This is a test response from Mistral AI.")
    
    @patch('modules.ai.mistral.client')
    def test_run_mistral_with_custom_model(self, mock_client):
        """Test run_mistral with a custom model parameter."""
        # Set up the mock response
        mock_choice = MagicMock()
        mock_choice.message.content = "Response from custom model."
        
        mock_response = MagicMock()
        mock_response.choices = [mock_choice]
        
        mock_client.chat.complete.return_value = mock_response
        
        # Call the function with a test prompt and custom model
        test_prompt = "Test prompt"
        custom_model = "mistral-tiny"
        response = run_mistral(test_prompt, model=custom_model)
        
        # Verify the client was called with the custom model
        call_args = mock_client.chat.complete.call_args[1]
        self.assertEqual(call_args['model'], custom_model)
        
        # Verify the response is correctly returned
        self.assertEqual(response, "Response from custom model.")
    
    @patch('modules.ai.mistral.MISTRAL_API_KEY', None)
    def test_run_mistral_without_api_key(self):
        """Test run_mistral raises an error when no API key is available."""
        with self.assertRaises(ValueError) as context:
            run_mistral("Test prompt")
        
        self.assertIn("MISTRAL_API_KEY not found", str(context.exception))


if __name__ == '__main__':
    unittest.main()
