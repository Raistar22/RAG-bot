#!/bin/bash

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies one by one
pip install streamlit==1.32.0
pip install requests==2.31.0
pip install beautifulsoup4==4.12.2
pip install langchain==0.1.12
pip install faiss-cpu==1.7.4
pip install sentence-transformers==2.5.1
pip install python-docx==1.0.1
pip install pypdf==3.17.1
pip install huggingface-hub==0.21.4
pip install torch==2.2.0 --index-url https://download.pytorch.org/whl/cpu
pip install transformers==4.37.2
pip install numpy==1.26.4
pip install tqdm==4.66.1
pip install safetensors==0.4.2
pip install accelerate==0.27.2

# Install the package in development mode
pip install -e . 