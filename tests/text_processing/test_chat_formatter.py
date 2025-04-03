"""
Unit tests for the chat formatter module.
"""

import unittest
import os
import tempfile
from modules.text_processing.chat_formatter import format_chat_log_to_md, save_formatted_chat

class TestChatFormatter(unittest.TestCase):
    
    def setUp(self):
        """Set up test data that will be used by the test methods."""
        self.test_chat_log = """
        Some header content
        You said:
        # **You said:**
        This is a test message I sent.
        # **ChatGPT said:**
        This is a response from the AI assistant.
        # **You said:**
        Another message from me.
        # **ChatGPT said:**
        Another response from the assistant.
        4o Search Deep research
        Some footer content
        """
    
    def test_format_chat_log_to_md(self):
        """Test chat log formatting to markdown."""
        formatted_text = format_chat_log_to_md(self.test_chat_log)
        
        # Verify the formatted output contains expected content
        self.assertIn("# You said:", formatted_text)
        self.assertIn("This is a test message I sent.", formatted_text)
        self.assertIn("# ChatGPT said:", formatted_text)
        self.assertIn("This is a response from the AI assistant.", formatted_text)
        
        # Verify unwanted content is removed
        self.assertNotIn("Some header content", formatted_text)
        self.assertNotIn("4o Search Deep research", formatted_text)
        self.assertNotIn("Some footer content", formatted_text)
        
        # Verify the markdown format is correct (no double asterisks)
        self.assertNotIn("**You said:**", formatted_text)
        self.assertNotIn("**ChatGPT said:**", formatted_text)
    
    def test_format_chat_log_invalid_input(self):
        """Test handling of input without the expected markers."""
        invalid_input = "This is some text without the expected chat markers."
        formatted_text = format_chat_log_to_md(invalid_input)
        
        # Should return empty string for invalid input
        self.assertEqual(formatted_text, "")
    
    def test_save_formatted_chat(self):
        """Test saving formatted chat to a file."""
        test_content = "# Test formatted chat\nThis is test content."
        
        # Create a temporary file for testing
        with tempfile.NamedTemporaryFile(delete=False, suffix='.md') as temp:
            temp_filename = temp.name
        
        try:
            # Save the formatted chat to the temporary file
            result = save_formatted_chat(test_content, temp_filename)
            
            # Verify the function returned True (success)
            self.assertTrue(result)
            
            # Verify the file was created and contains the expected content
            with open(temp_filename, 'r', encoding='utf-8') as f:
                file_content = f.read()
            
            self.assertEqual(file_content, test_content)
            
        finally:
            # Clean up: remove the temporary file
            if os.path.exists(temp_filename):
                os.remove(temp_filename)


if __name__ == '__main__':
    unittest.main()
