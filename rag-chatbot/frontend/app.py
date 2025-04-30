import streamlit as st
import os
import sys
from pathlib import Path

# Get the absolute path of the current file
current_dir = Path(__file__).resolve().parent
# Add the parent directory to the Python path
sys.path.append(str(current_dir.parent))

try:
    from backend.app import build_qa_chain
except ImportError:
    st.error("Error: Could not import backend module. Please check the deployment structure.")
    st.stop()

st.title("📋 RAG Chatbot for Insurance & Angel One Support")

try:
    qa_chain = build_qa_chain()
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
