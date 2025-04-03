# AI Agent Frontend

A modular Streamlit application for AI-driven text processing and content generation.

## Features

- **Mistral AI Integration**: Generate text responses using Mistral AI's large language model
- **HTML Scraping**: Extract text and links from HTML content
- **Text Organization**: Clean and organize copied text
- **Markdown Processing**: Read and analyze markdown files
- **Chat Log Formatting**: Convert raw chat logs to clean markdown format

## Project Structure

```
ai_agent/
├── app.py                  # Main Streamlit application
├── modules/                # Core functionality modules
│   ├── ai/                 # AI integration modules
│   │   ├── __init__.py
│   │   └── mistral.py      # Mistral AI API integration
│   ├── text_processing/    # Text processing modules
│   │   ├── __init__.py
│   │   ├── chat_formatter.py  # Chat log formatting
│   │   ├── copy_paste.py   # Text organization
│   │   └── html_scraper.py # HTML content extraction
│   └── file_operations/    # File handling modules
│       ├── __init__.py
│       └── markdown_reader.py  # Markdown file processing
├── utils/                  # Utility functions
│   ├── __init__.py
│   └── config.py           # Configuration and environment variables
├── tests/                  # Test modules
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (not in version control)
└── README.md               # Project documentation
```

## Getting Started

1. Clone the repository: `git clone https://github.com/ruizTechServices/ai_agent.git`
2. Change into the repository: `cd ai_agent`
3. Create a virtual environment: `python -m venv .venv`
4. Activate the virtual environment:
    * On macOS/Linux: `source .venv/bin/activate`
    * On Windows (CMD): `.venv\Scripts\activate`
    * On Windows (PowerShell): `.venv\Scripts\Activate.ps1`
5. Install the required packages: `pip install -r requirements.txt`
6. Copy `.env.example` to `.env` and add your API keys
7. Run the application: `streamlit run app.py`

## Environment Variables

Create a `.env` file in the project root with the following variables:

```
MISTRAL_API_KEY=your_mistral_api_key_here
```

## Development

### Adding New Features

To add a new feature:

1. Create a new module in the appropriate folder
2. Import and integrate it in app.py
3. Add tests for the new functionality

### Running Tests

Run tests with pytest:

```
python -m pytest tests/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
