"""
Markdown file reader module.
Provides functions to read and parse markdown files.
"""

def read_markdown_file(file_content: str) -> str:
    """
    Read a markdown file content and return it.
    
    Args:
        file_content (str): The content of the markdown file
        
    Returns:
        str: The file content
    """
    return file_content


def extract_headings(markdown_content: str) -> list:
    """
    Extract all headings from markdown content.
    
    Args:
        markdown_content (str): The markdown content
        
    Returns:
        list: List of dictionaries containing heading level and text
    """
    headings = []
    lines = markdown_content.splitlines()
    
    for line in lines:
        line = line.strip()
        # Check for markdown headings (# Heading)
        if line.startswith('#'):
            # Count the number of # to determine heading level
            level = 0
            for char in line:
                if char == '#':
                    level += 1
                else:
                    break
            
            # Extract the heading text
            heading_text = line[level:].strip()
            
            headings.append({
                'level': level,
                'text': heading_text
            })
    
    return headings


if __name__ == '__main__':
    # Example usage when run directly
    test_md = """# Main Heading
    
This is some content.

## Sub Heading

More content here.

### Sub-sub heading

Even more content.
"""
    
    print("Extracting headings:")
    headings = extract_headings(test_md)
    for heading in headings:
        print(f"Level {heading['level']}: {heading['text']}")
