import streamlit as st
import os
import sys
from pathlib import Path

# Get the absolute path of the current file
current_dir = Path(__file__).resolve().parent
# Add the parent directory to the Python path
sys.path.insert(0, str(current_dir.parent))

# Debug information
st.write("Current directory:", current_dir)
st.write("Python path:", sys.path)

# Check for required packages
required_packages = ['langchain', 'faiss-cpu', 'sentence-transformers', 'huggingface-hub']
missing_packages = []

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        missing_packages.append(package)

if missing_packages:
    st.error("Missing required packages. Please install them using:")
    st.code(f"pip install {' '.join(missing_packages)}")
    st.error("Or make sure requirements.txt is properly set up in your deployment.")
    st.stop()

try:
    from backend.app import build_qa_chain
    st.write("Successfully imported backend module")
except ImportError as e:
    st.error(f"Import Error: {str(e)}")
    st.error("Current directory contents:")
    for item in os.listdir(current_dir.parent):
        st.write(f"- {item}")
    st.stop()

st.title("📋 RAG Chatbot for Insurance & Angel One Support")

try:
    qa_chain = build_qa_chain()
    st.write("Successfully initialized QA chain")
except Exception as e:
    st.error(f"Error initializing QA chain: {str(e)}")
    st.stop()

query = st.text_input("Ask a question based on the insurance PDFs or Angel One Support:")
if query:
    try:
        result = qa_chain(query)
        answer = result['result'].strip()
        if "I don't know" in answer or len(answer) < 10:
            st.warning("I don't know")
        else:
            st.success(answer)
    except Exception as e:
        st.error(f"Error processing query: {str(e)}")
