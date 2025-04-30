from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
import os

def build_qa_chain():
    # Initialize embeddings
    embeddings = HuggingFaceEmbeddings()
    
    # Load the vector store
    vectorstore_path = "vectorstore"
    if not os.path.exists(vectorstore_path):
        raise Exception("Vector store not found. Please run the scraper first.")
    
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