"""
Unit tests for the HTML scraper module.
"""

import unittest
from modules.text_processing.html_scraper import extract_text_from_html, extract_links_from_html

class TestHtmlScraper(unittest.TestCase):
    
    def setUp(self):
        """Set up test data that will be used by the test methods."""
        self.test_html = """
        <html>
            <body>
                <h1>Test Header</h1>
                <p>This is a <b>test</b> paragraph.</p>
                <a href="https://example.com">Example Link</a>
                <a href="https://test.com">Test Link</a>
            </body>
        </html>
        """
    
    def test_extract_text_from_html(self):
        """Test that text extraction correctly removes HTML tags and preserves content."""
        extracted_text = extract_text_from_html(self.test_html)
        
        # Verify the text extraction
        self.assertIn("Test Header", extracted_text)
        self.assertIn("This is a test paragraph", extracted_text)
        self.assertIn("Example Link", extracted_text)
        
        # Verify HTML tags are removed
        self.assertNotIn("<h1>", extracted_text)
        self.assertNotIn("<p>", extracted_text)
        self.assertNotIn("<b>", extracted_text)
    
    def test_extract_links_from_html(self):
        """Test that link extraction correctly identifies all links in the HTML."""
        extracted_links = extract_links_from_html(self.test_html)
        
        # Verify we found two links
        self.assertEqual(len(extracted_links), 2)
        
        # Verify the first link details
        self.assertEqual(extracted_links[0]['text'], 'Example Link')
        self.assertEqual(extracted_links[0]['href'], 'https://example.com')
        
        # Verify the second link details
        self.assertEqual(extracted_links[1]['text'], 'Test Link')
        self.assertEqual(extracted_links[1]['href'], 'https://test.com')
    
    def test_extract_text_from_empty_html(self):
        """Test handling of empty HTML content."""
        extracted_text = extract_text_from_html("")
        self.assertEqual(extracted_text, "")
    
    def test_extract_links_from_html_no_links(self):
        """Test link extraction when there are no links in the HTML."""
        html_without_links = "<html><body><p>No links here</p></body></html>"
        extracted_links = extract_links_from_html(html_without_links)
        self.assertEqual(len(extracted_links), 0)


if __name__ == '__main__':
    unittest.main()
