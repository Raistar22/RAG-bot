# RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that uses web scraping to gather information from Angel One's support website.

## Features

- Web scraping of Angel One support pages
- Data processing and storage
- RAG-based question answering system

## Project Structure

```
rag-chatbot/
├── backend/
│   ├── app.py          # Main application code
│   ├── parser.py       # Document parsing utilities
│   └── scrape_webpages.py  # Web scraping functionality
├── data/
│   └── webpages/       # Scraped webpage content
└── README.md
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Raistar22/RAG-bot.git
cd RAG-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the web scraper:
```bash
python backend/scrape_webpages.py
```

## Requirements

- Python 3.8+
- requests
- beautifulsoup4
- langchain
- faiss-cpu
- sentence-transformers
- python-docx
- pypdf

## License

MIT License 