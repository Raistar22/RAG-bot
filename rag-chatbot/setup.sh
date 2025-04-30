#!/bin/bash

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies with specific indexes
pip install -r requirements.txt --no-cache-dir

# Install the package in development mode
pip install -e . --no-cache-dir 