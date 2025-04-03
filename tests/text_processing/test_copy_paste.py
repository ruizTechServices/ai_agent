"""
Unit tests for the copy-paste organizer module.
"""

import unittest
from modules.text_processing.copy_paste import organize_copied_text, add_ignore_phrase, IGNORE_PHRASES

class TestCopyPaste(unittest.TestCase):
    
    def setUp(self):
        """Set up test data that will be used by the test methods."""
        self.test_text = """
        Skip to Content
        Menu
        App Router
        
        This is some important content that should be kept.
        
        More important information is here.
        
        © 2023 Vercel Inc.
        """
        
        # Store the original IGNORE_PHRASES for restoration after tests
        self.original_ignore_phrases = IGNORE_PHRASES.copy()
    
    def tearDown(self):
        """Clean up after each test method."""
        # Restore the original IGNORE_PHRASES
        global IGNORE_PHRASES
        IGNORE_PHRASES.clear()
        IGNORE_PHRASES.extend(self.original_ignore_phrases)
    
    def test_organize_copied_text(self):
        """Test that the text organizer removes ignored phrases."""
        organized_text = organize_copied_text(self.test_text)
        
        # Verify ignored phrases are removed
        self.assertNotIn("Skip to Content", organized_text)
        self.assertNotIn("Menu", organized_text)
        self.assertNotIn("App Router", organized_text)
        self.assertNotIn("© 2023 Vercel Inc.", organized_text)
        
        # Verify important content is preserved
        self.assertIn("This is some important content that should be kept", organized_text)
        self.assertIn("More important information is here", organized_text)
    
    def test_add_ignore_phrase(self):
        """Test adding a new phrase to the ignore list."""
        # Add a new phrase to ignore
        new_phrase = "Test Phrase to Ignore"
        add_ignore_phrase(new_phrase)
        
        # Verify the phrase was added
        self.assertIn(new_phrase, IGNORE_PHRASES)
        
        # Test with a text containing the new ignore phrase
        test_text_with_new_phrase = """
        Test Phrase to Ignore
        This is important content.
        """
        
        organized_text = organize_copied_text(test_text_with_new_phrase)
        
        # Verify the new ignore phrase is removed
        self.assertNotIn("Test Phrase to Ignore", organized_text)
        
        # Verify important content is preserved
        self.assertIn("This is important content", organized_text)
    
    def test_add_duplicate_ignore_phrase(self):
        """Test that adding a duplicate ignore phrase doesn't change the list."""
        initial_length = len(IGNORE_PHRASES)
        
        # Try to add a phrase that's already in the list
        add_ignore_phrase("menu")  # 'menu' is already in IGNORE_PHRASES
        
        # Verify the length hasn't changed
        self.assertEqual(len(IGNORE_PHRASES), initial_length)
    
    def test_empty_text(self):
        """Test organizing empty text."""
        organized_text = organize_copied_text("")
        self.assertEqual(organized_text, "")


if __name__ == '__main__':
    unittest.main()
