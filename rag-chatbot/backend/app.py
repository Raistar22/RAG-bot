from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
import os
from pathlib import Path

def build_qa_chain():
    # Get the absolute path of the current file
    current_dir = Path(__file__).resolve().parent
    parent_dir = current_dir.parent
    
    # Initialize embeddings
    embeddings = HuggingFaceEmbeddings()
    
    # Load the vector store
    vectorstore_path = os.path.join(parent_dir, "vectorstore")
    if not os.path.exists(vectorstore_path):
        raise Exception(f"Vector store not found at {vectorstore_path}. Please run the scraper first.")
    
    vectorstore = FAISS.load_local(vectorstore_path, embeddings)
    
    # Initialize the LLM
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-large",
        model_kwargs={"temperature": 0.7, "max_length": 512}
    )
    
    # Create the QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
    )
    
    return qa_chain 