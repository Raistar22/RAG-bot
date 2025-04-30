#!/bin/bash

# Upgrade pip
python -m pip install --upgrade pip

# Install base dependencies first
pip install numpy==1.24.3
pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install transformers==4.35.2
pip install sentence-transformers==2.2.2
pip install faiss-cpu==1.7.4
pip install huggingface-hub==0.19.4
pip install langchain==0.0.350

# Install other dependencies
pip install streamlit==1.32.0
pip install requests==2.31.0
pip install beautifulsoup4==4.12.2
pip install python-docx==1.0.1
pip install pypdf==3.17.1
pip install tqdm==4.66.1
pip install safetensors==0.4.1
pip install accelerate==0.24.1

# Install the package in development mode
pip install -e . 