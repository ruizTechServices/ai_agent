# organize_chat_convo.py
import re
import os

def format_chat_log_to_md(raw_text: str) -> str:
    """
    Formats raw chat text into a clean Markdown string.

    Extracts alternating "You said:" and "ChatGPT said:" sections,
    removes specified header and footer text based on markers,
    and formats the output for a .md file.

    Args:
        raw_text: The raw chat text input string.

    Returns:
        A formatted string in Markdown, ready to be saved to a .md file,
        or an empty string if no valid chat content is found.
    """
    # 1. Define markers
    start_marker = "You said:"
    footer_marker = "4o Search Deep research"
    splitter_pattern = r'(# \*\*You said:\*\*|# \*\*ChatGPT said:\*\*)'

    # 2. Remove header
    start_index = raw_text.find(start_marker)
    if start_index >= 1:
        processed_text = raw_text[start_index + len(start_marker):].strip()
    else:
        print("Start marker not found. No formatting applied.")
        # If the start marker is not found, return an empty string
        return processed_text

    # 3. Remove footer
    footer_index = processed_text.find(footer_marker)
    if footer_index != -1:
        processed_text = processed_text[:footer_index]
        processed_text = processed_text.rstrip()

    # 4. Split the processed text
    parts = re.split(splitter_pattern, processed_text)

    # 5. Process the parts
    formatted_blocks = []
    for i in range(1, len(parts), 2):
        marker = parts[i]
        content = parts[i+1].strip() if (i+1) < len(parts) else ""
        if marker == "# **You said:**":
            formatted_blocks.append(f"# You said:\n{content}")
        elif marker == "# **ChatGPT said:**":
            formatted_blocks.append(f"# ChatGPT said:\n{content}")

    # 6. Join the formatted blocks
    final_output = "\n\n".join(formatted_blocks)
    return final_output

# --- Example Usage section for running this file directly ---
if __name__ == "__main__":
    format_chat_log_to_md()
    # Exampl

    # # Optional: Save to file
    # output_filename = "formatted_chat_example.md"
    # try:
    #     with open(output_filename, "w", encoding="utf-8") as f:
    #         f.write(formatted_text_example)
    #     print(f"\nFormatted example text saved to {output_filename}")
    # except Exception as e:
    #     print(f"\nError saving file: {e}")