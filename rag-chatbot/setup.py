from setuptools import setup, find_packages

setup(
    name="rag-chatbot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit==1.32.0",
        "requests==2.32.3",
        "beautifulsoup4==4.12.3",
        "langchain==0.1.12",
        "faiss-cpu==1.7.4",
        "sentence-transformers==2.5.1",
        "python-docx==1.1.2",
        "pypdf==5.4.0",
        "huggingface-hub==0.21.4",
        "torch==2.2.0",
        "transformers==4.37.2",
        "numpy>=1.24.0",
        "tqdm>=4.66.1",
        "safetensors>=0.4.2",
        "accelerate>=0.27.2",
    ],
    python_requires=">=3.8",
) 