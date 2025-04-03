# app.py
import streamlit as st

try:
    from copy_paste_organizer import organize_copied_text
except ImportError:
    def organize_copied_text(text: str) -> str: return f"Placeholder for organize_copied_text: {text}"

try:
    from mistal_endpoint import run_mistral
except ImportError:
    def run_mistral(prompt: str) -> str: return f"Placeholder for run_mistral: {prompt}"

try:
    from organize_chat_convo import format_chat_log_to_md
except ImportError:
    st.error("Fatal Error: Could not import 'format_chat_log_to_md' from 'organize_chat_convo.py'. App cannot function correctly.")
    def format_chat_log_to_md(text: str) -> str: return "ERROR: Chat formatting function not loaded."
    st.stop()

from bs4 import BeautifulSoup

st.title("AI Agent Frontend")

function_list = [
    "Run Mistral",
    "Scrape HTML",
    "Organize Copied Text",
    "Read Markdown File",
    "Format Chat Log to Markdown"
]
function_choice = st.sidebar.selectbox("Select Function", function_list)

if function_choice == "Run Mistral":
    st.header("Run Mistral")
    user_input = st.text_area("Enter your message here", height=150, key="mistral_input")
    if st.button("Send", key="mistral_send"):
        if user_input:
            try:
                response = run_mistral(user_input)
                st.subheader("Response:")
                st.markdown(response)
            except Exception as e:
                st.error(f"An error occurred while running Mistral: {e}")
        else:
            st.warning("Please enter a message.")

elif function_choice == "Scrape HTML":
    st.header("Scrape HTML Content")
    html_input = st.text_area("Enter HTML content here", height=300, key="html_input")
    if st.button("Extract Text", key="extract_html"):
        if html_input:
            try:
                soup = BeautifulSoup(html_input, "html.parser")
                extracted_text = soup.get_text(separator=" ", strip=True)
                st.subheader("Extracted Text:")
                st.text_area("Result", value=extracted_text, height=300, key="html_output")
            except Exception as e:
                st.error(f"An error occurred during HTML parsing: {e}")
        else:
            st.warning("Please enter HTML content.")

elif function_choice == "Organize Copied Text":
    st.header("Organize Copied Text")
    copied_text = st.text_area("Paste your copied text here", height=300, key="copied_text_input")
    if st.button("Organize Text", key="organize_text"):
        if copied_text:
            try:
                organized_output = organize_copied_text(copied_text)
                st.subheader("Organized Text (Rendered):")
                st.markdown(organized_output)
                st.subheader("Organized Text (Raw Markdown):")
                st.code(organized_output, language='markdown')
            except Exception as e:
                st.error(f"An error occurred during text organization: {e}")
        else:
            st.warning("Please paste some text.")

elif function_choice == "Read Markdown File":
    st.header("Read Markdown File")
    md_file = st.file_uploader("Upload a Markdown file", type=["md"], key="md_uploader")
    if md_file is not None:
        try:
            md_content = md_file.read().decode('utf-8')
            st.subheader("Markdown File Content:")
            st.markdown(md_content)
        except Exception as e:
            st.error(f"Error reading or decoding file: {e}")

elif function_choice == "Format Chat Log to Markdown":
    st.header("Format Raw Chat Log")
    chat_log_input = st.text_area("Paste the raw chat log text here:", height=300, key="chat_log_input")
    if st.button("Format Chat Log", key="format_chat_button"):
        if chat_log_input:
            try:
                formatted_output = format_chat_log_to_md(chat_log_input)

                if formatted_output:
                    st.subheader("Formatted Chat Log (Rendered):")
                    st.markdown(formatted_output)
                    st.subheader("Formatted Chat Log (Raw Markdown):")
                    st.code(formatted_output, language='markdown')
                else:
                    st.warning("Formatting resulted in empty output. Please ensure the input text contains '# **You said:**' and follows the expected structure.")
            except Exception as e:
                st.error(f"An error occurred during chat log formatting: {e}")
        else:
            st.warning("Please paste your chat log text first.")
