#!/bin/bash

# Deploy MFA System

echo "Deploying MFA System..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install pyotp

# Run MFA system
python3 src/mfa_system.py

echo "Deployment Completed."
