# backend/parser.py

from pathlib import Path
from pypdf import PdfReader
import docx
import requests
from bs4 import BeautifulSoup

def load_insurance_documents(pdf_folder: str, docx_file: str):
    documents = []

    # Load PDFs
    for pdf_path in Path(pdf_folder).glob("*.pdf"):
        try:
            reader = PdfReader(pdf_path)
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
            documents.append((pdf_path.name, text))
        except Exception as e:
            print(f"[ERROR] Failed to read {pdf_path}: {e}")

    # Load DOCX
    try:
        doc = docx.Document(docx_file)
        doc_text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
        documents.append((Path(docx_file).name, doc_text))
    except Exception as e:
        print(f"[ERROR] Failed to read DOCX file: {e}")

    return documents


def scrape_angelone_support(base_url="https://www.angelone.in/support", max_links=20):
    """
    Scrapes FAQ content from angelone.in/support. Only scrapes a limited number of links.
    """
    documents = []
    try:
        res = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(res.content, "html.parser")
        links = list({a['href'] for a in soup.select("a[href^='/support/']") if '/support/' in a['href']})
        links = links[:max_links]  # Limit to avoid scraping too much

        for link in links:
            full_url = f"https://www.angelone.in{link}"
            try:
                page = requests.get(full_url, timeout=10)
                s = BeautifulSoup(page.content, "html.parser")
                title = s.title.text.strip() if s.title else link
                body = " ".join([p.get_text(strip=True) for p in s.find_all("p")])
                documents.append((title, body))
            except Exception as e:
                print(f"[WARN] Failed to scrape {full_url}: {e}")

    except Exception as e:
        print(f"[ERROR] Failed to access Angel One support page: {e}")

    return documents
