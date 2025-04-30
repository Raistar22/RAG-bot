import streamlit as st
import os
import sys
from pathlib import Path

# Get the absolute path of the current file
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent

# Add the parent directory to the Python path
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

# Debug information
st.write("Current directory:", current_dir)
st.write("Parent directory:", parent_dir)
st.write("Python path:", sys.path)
st.write("Python version:", sys.version)

# Try to import required packages with fallbacks
try:
    import langchain
    st.write("Successfully imported langchain")
except ImportError as e:
    st.error(f"Error importing langchain: {str(e)}")
    st.stop()

try:
    import faiss
    st.write("Successfully imported faiss")
except ImportError as e:
    st.error(f"Error importing faiss: {str(e)}")
    st.stop()

try:
    import sentence_transformers
    st.write("Successfully imported sentence-transformers")
except ImportError as e:
    st.error(f"Error importing sentence-transformers: {str(e)}")
    st.stop()

try:
    import huggingface_hub
    st.write("Successfully imported huggingface-hub")
except ImportError as e:
    st.error(f"Error importing huggingface-hub: {str(e)}")
    st.stop()

try:
    from backend.app import build_qa_chain
    st.write("Successfully imported backend module")
except ImportError as e:
    st.error(f"Import Error: {str(e)}")
    st.error("Current directory contents:")
    for item in os.listdir(parent_dir):
        st.write(f"- {item}")
    st.error("Backend directory contents:")
    if os.path.exists(os.path.join(parent_dir, "backend")):
        for item in os.listdir(os.path.join(parent_dir, "backend")):
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
