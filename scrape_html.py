from bs4 import BeautifulSoup
import sys


def main():
    print("Enter your HTML input. Press Ctrl-D (Unix/macOS) or Ctrl-Z (Windows) followed by Enter to finish:")
    html = sys.stdin.read()
    
    # Parse the user-provided HTML
    soup = BeautifulSoup(html, "html.parser")
    
    # Extract all text from the HTML input
    text = soup.get_text(separator=" ", strip=True)
    
    print("\nExtracted text:\n")
    print(text)


if __name__ == '__main__':
    main()