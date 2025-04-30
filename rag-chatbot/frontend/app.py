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

# Check installed packages
try:
    import pkg_resources
    installed_packages = [d.project_name for d in pkg_resources.working_set]
    st.write("Installed packages:", installed_packages)
except ImportError:
    st.warning("Could not check installed packages")

# Try to import required packages
required_packages = {
    'langchain': 'langchain',
    'faiss': 'faiss-cpu',
    'sentence_transformers': 'sentence-transformers',
    'huggingface_hub': 'huggingface-hub'
}

missing_packages = []
for module_name, package_name in required_packages.items():
    try:
        __import__(module_name)
        st.write(f"Successfully imported {package_name}")
    except ImportError as e:
        st.write(f"Error importing {package_name}: {str(e)}")
        missing_packages.append(package_name)

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
