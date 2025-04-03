import re

# Global constant for phrases to ignore (for case-insensitive matching)
IGNORE_PHRASES = [
    'skip to content',
    'menu',
    'app router',
    'getting started',
    'installation',
    'automatic installation',
    'manual installation',
    'create a new next.js app',
    'resources',
    'your feedback',
    '©',
    'subscribe',
    'contact',
    'community',
    'docs',
    'support policy',
    'blog',
    'about vercel',
    'next.js + vercel'
]

def organize_copied_text(text: str) -> str:
    """
    Organizes the copied text by removing header and footer content (like navigation links)
    using simple heuristics based on common phrases.

    Parameters:
        text (str): The raw copied text that may contain headers, footers, and other extraneous content.

    Returns:
        str: The cleaned text with only the main content.
    """
    # Split the input text into lines and filter them
    filtered_lines = [
        line.strip() for line in text.splitlines()
        if line.strip() and not any(phrase in line.strip().lower() for phrase in IGNORE_PHRASES)
    ]
    
    # Join the filtered lines with newline characters and then collapse multiple whitespace characters
    cleaned_text = "\n".join(filtered_lines)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

def format_cleaned_text(text: str) -> str:
    """
    Formats the cleaned text into a more organized, readable format.
    This implementation uses simple heuristics:
      - Lines that are short (under 50 characters) and do not end with punctuation are treated as headings.
      - All other lines are prefixed with a bullet point.
    
    Parameters:
        text (str): The cleaned text to format.

    Returns:
        str: The formatted text with headings and bullet points.
    """
    lines = text.split("\n")
    formatted_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # If the line is short and doesn't end with punctuation, treat it as a heading
        if len(line) < 50 and (line[-1] not in '.?!'):
            formatted_lines.append(f"### {line}")
        else:
            formatted_lines.append(f"- {line}")
    
    return "\n\n".join(formatted_lines)



if __name__ == '__main__':
    pass