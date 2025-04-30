#!/bin/bash

# Create and activate Python 3.10 virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Install PyTorch with specific versions for Python 3.10
pip install --no-cache-dir torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cpu

# Verify installation
python -c "import torch; print('PyTorch version:', torch.__version__)"
python -c "import torch; print('CUDA available:', torch.cuda.is_available())"
python -c "import torch; print('Device:', torch.device('cpu'))" 