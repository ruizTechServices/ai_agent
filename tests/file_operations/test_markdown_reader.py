"""
Unit tests for the markdown reader module.
"""

import unittest
from modules.file_operations.markdown_reader import read_markdown_file, extract_headings

class TestMarkdownReader(unittest.TestCase):
    
    def setUp(self):
        """Set up test data that will be used by the test methods."""
        self.test_markdown = """# Main Heading

This is some content.

## Sub Heading

More content here.

### Sub-sub heading

Even more content.
"""
    
    def test_read_markdown_file(self):
        """Test reading markdown file content."""
        content = read_markdown_file(self.test_markdown)
        
        # Verify the content is returned unchanged
        self.assertEqual(content, self.test_markdown)
    
    def test_extract_headings(self):
        """Test extracting headings from markdown content."""
        headings = extract_headings(self.test_markdown)
        
        # Verify the number of headings found
        self.assertEqual(len(headings), 3)
        
        # Verify the first heading (level 1)
        self.assertEqual(headings[0]['level'], 1)
        self.assertEqual(headings[0]['text'], 'Main Heading')
        
        # Verify the second heading (level 2)
        self.assertEqual(headings[1]['level'], 2)
        self.assertEqual(headings[1]['text'], 'Sub Heading')
        
        # Verify the third heading (level 3)
        self.assertEqual(headings[2]['level'], 3)
        self.assertEqual(headings[2]['text'], 'Sub-sub heading')
    
    def test_extract_headings_no_headings(self):
        """Test extracting headings from markdown with no headings."""
        markdown_no_headings = """This is some text.
        
        It has no headings.
        
        Just paragraphs.
        """
        headings = extract_headings(markdown_no_headings)
        
        # Verify no headings were found
        self.assertEqual(len(headings), 0)
    
    def test_extract_headings_complex_formats(self):
        """Test extracting headings with more complex formats."""
        complex_markdown = """# Heading with *italic*
        
        ## Heading with **bold**
        
        ### Heading with `code`
        
        #### Heading with [link](https://example.com)
        """
        headings = extract_headings(complex_markdown)
        
        # Verify all headings were found
        self.assertEqual(len(headings), 4)
        
        # Verify the heading text includes formatting characters
        self.assertEqual(headings[0]['text'], 'Heading with *italic*')
        self.assertEqual(headings[1]['text'], 'Heading with **bold**')
        self.assertEqual(headings[2]['text'], 'Heading with `code`')
        self.assertEqual(headings[3]['text'], 'Heading with [link](https://example.com)')


if __name__ == '__main__':
    unittest.main()
