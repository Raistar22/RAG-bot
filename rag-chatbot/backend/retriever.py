# backend/retriever.py

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

from backend.parser import load_insurance_documents, scrape_angelone_support

def load_and_prepare_documents():
    # Load insurance files
    pdf_folder = "data/insurance_pdfs"
    docx_path = "data/America's_Choice_Medical_Questions_-_Modified_(3) (1).docx"
    insurance_docs = load_insurance_documents(pdf_folder, docx_path)

    # Scrape AngelOne support pages
    web_docs = scrape_angelone_support()

    # Combine all
    return insurance_docs + web_docs


def prepare_embeddings():
    documents = load_and_prepare_documents()

    # Convert to LangChain Document format
    lc_docs = [Document(page_content=text, metadata={"source": name}) for name, text in documents]

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(lc_docs)

    # Embedding model
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Vector DB
    db = FAISS.from_documents(chunks, embedding_model)
    db.save_local("vectorstore")

    return db
