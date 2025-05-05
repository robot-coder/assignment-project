#!/bin/bash
# Deployment script for Chat Assistant on Render

# Clone repository
git clone https://github.com/yourusername/lab02.git
cd lab02

# Setup environment and dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run deployment commands specific to Render setup
# (e.g., start server, specify environment variables)

# Placeholder for start command
# python chat_assistant.py

echo "Deployment script executed."