"""
HTML scraper module.
Provides functions to extract text content from HTML.
"""

from bs4 import BeautifulSoup

def extract_text_from_html(html_content: str) -> str:
    """
    Extract all text content from HTML, removing HTML tags.
    
    Args:
        html_content (str): The HTML content to process
        
    Returns:
        str: The extracted text with HTML tags removed
        
    Raises:
        Exception: If there is an error parsing the HTML
    """
    try:
        # Parse the HTML
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Extract all text from the HTML, preserving some whitespace structure
        extracted_text = soup.get_text(separator=" ", strip=True)
        
        return extracted_text
    except Exception as e:
        raise Exception(f"Error parsing HTML: {e}")


def extract_links_from_html(html_content: str) -> list:
    """
    Extract all links (href attributes) from HTML content.
    
    Args:
        html_content (str): The HTML content to process
        
    Returns:
        list: List of dictionaries containing link text and href
    """
    links = []
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Find all <a> tags with href attributes
        for a_tag in soup.find_all('a', href=True):
            links.append({
                'text': a_tag.get_text(strip=True),
                'href': a_tag['href']
            })
            
        return links
    except Exception as e:
        print(f"Error extracting links: {e}")
        return []


if __name__ == '__main__':
    # Example usage when run directly
    test_html = """
    <html>
        <body>
            <h1>Test Header</h1>
            <p>This is a <b>test</b> paragraph.</p>
            <a href="https://example.com">Example Link</a>
        </body>
    </html>
    """
    
    text = extract_text_from_html(test_html)
    print("Extracted text:")
    print(text)
    
    links = extract_links_from_html(test_html)
    print("\nExtracted links:")
    for link in links:
        print(f"Text: {link['text']}, URL: {link['href']}")
