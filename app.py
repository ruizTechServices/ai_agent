"""
AI Agent Frontend - Main Application Entry Point

This is the main Streamlit application that provides a user interface
for various AI agent functionalities.
"""

import streamlit as st

# Import modules
from modules.ai.mistral import run_mistral
from modules.text_processing.copy_paste import organize_copied_text
from modules.text_processing.chat_formatter import format_chat_log_to_md
from modules.text_processing.html_scraper import extract_text_from_html, extract_links_from_html
from modules.file_operations.markdown_reader import read_markdown_file, extract_headings

# Application title
st.title("AI Agent Frontend")

# Function selection in sidebar
function_list = [
    "Run Mistral",
    "Scrape HTML",
    "Organize Copied Text",
    "Read Markdown File",
    "Format Chat Log to Markdown"
]
function_choice = st.sidebar.selectbox("Select Function", function_list)

# Run Mistral AI Integration
if function_choice == "Run Mistral":
    st.header("Run Mistral")
    user_input = st.text_area("Enter your message here", height=150, key="mistral_input")
    if st.button("Send", key="mistral_send"):
        if user_input:
            try:
                with st.spinner("Generating response..."):
                    response = run_mistral(user_input)
                st.subheader("Response:")
                st.markdown(response)
            except Exception as e:
                st.error(f"An error occurred while running Mistral: {e}")
        else:
            st.warning("Please enter a message.")

# HTML Scraping
elif function_choice == "Scrape HTML":
    st.header("Scrape HTML Content")
    html_input = st.text_area("Enter HTML content here", height=300, key="html_input")
    
    col1, col2 = st.columns(2)
    with col1:
        extract_text = st.button("Extract Text", key="extract_text")
    with col2:
        extract_links = st.button("Extract Links", key="extract_links")
    
    if extract_text:
        if html_input:
            try:
                extracted_text = extract_text_from_html(html_input)
                st.subheader("Extracted Text:")
                st.text_area("Result", value=extracted_text, height=300, key="html_output")
            except Exception as e:
                st.error(f"An error occurred during HTML parsing: {e}")
        else:
            st.warning("Please enter HTML content.")
    
    if extract_links:
        if html_input:
            try:
                links = extract_links_from_html(html_input)
                st.subheader("Extracted Links:")
                if links:
                    for i, link in enumerate(links):
                        st.markdown(f"{i+1}. [{link['text']}]({link['href']})")
                else:
                    st.info("No links found in the provided HTML.")
            except Exception as e:
                st.error(f"An error occurred extracting links: {e}")
        else:
            st.warning("Please enter HTML content.")

# Copy-Paste Text Organization
elif function_choice == "Organize Copied Text":
    st.header("Organize Copied Text")
    copied_text = st.text_area("Paste your copied text here", height=300, key="copied_text_input")
    if st.button("Organize Text", key="organize_text"):
        if copied_text:
            try:
                with st.spinner("Organizing text..."):
                    organized_output = organize_copied_text(copied_text)
                st.subheader("Organized Text (Rendered):")
                st.markdown(organized_output)
                st.subheader("Organized Text (Raw Markdown):")
                st.code(organized_output, language='markdown')
            except Exception as e:
                st.error(f"An error occurred during text organization: {e}")
        else:
            st.warning("Please paste some text.")

# Markdown File Reading
elif function_choice == "Read Markdown File":
    st.header("Read Markdown File")
    md_file = st.file_uploader("Upload a Markdown file", type=["md"], key="md_uploader")
    if md_file is not None:
        try:
            md_content = md_file.read().decode('utf-8')
            
            # Use our markdown reader module
            processed_content = read_markdown_file(md_content)
            
            st.subheader("Markdown File Content:")
            st.markdown(processed_content)
            
            # Extract and display headings
            headings = extract_headings(processed_content)
            if headings:
                st.subheader("Document Structure:")
                for heading in headings:
                    # Use indentation to show heading hierarchy
                    indent = '&nbsp;' * (heading['level'] - 1) * 4
                    st.markdown(f"{indent}• {heading['text']}")
        except Exception as e:
            st.error(f"Error reading or processing file: {e}")

# Chat Log Formatting
elif function_choice == "Format Chat Log to Markdown":
    st.header("Format Raw Chat Log")
    chat_log_input = st.text_area("Paste the raw chat log text here:", height=300, key="chat_log_input")
    if st.button("Format Chat Log", key="format_chat_button"):
        if chat_log_input:
            try:
                with st.spinner("Formatting chat log..."):
                    formatted_output = format_chat_log_to_md(chat_log_input)

                if formatted_output:
                    st.subheader("Formatted Chat Log (Rendered):")
                    st.markdown(formatted_output)
                    st.subheader("Formatted Chat Log (Raw Markdown):")
                    st.code(formatted_output, language='markdown')
                    
                    # Add option to download the formatted chat
                    st.download_button(
                        label="Download Formatted Chat",
                        data=formatted_output,
                        file_name="formatted_chat.md",
                        mime="text/markdown"
                    )
                else:
                    st.warning("Formatting resulted in empty output. Please ensure the input text contains '# **You said:**' and follows the expected structure.")
            except Exception as e:
                st.error(f"An error occurred during chat log formatting: {e}")
        else:
            st.warning("Please paste your chat log text first.")

# Display app info in the sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown("### About")
    st.markdown("AI Agent Frontend provides a user interface for various AI-powered text processing tools.")
    st.markdown("Version 1.0")
