#!/bin/bash

# Install Python dependencies
python3 -m pip install -r requirements.txt

# Clear existing staticfiles
rm -rf staticfiles/*

# Collect static files
python3 manage.py collectstatic --noinput

# Ensure all static files are in staticfiles directory
if [ -d "static" ]; then
    cp -r static/* staticfiles/ 2>/dev/null || true
fi

# Create necessary directories
mkdir -p media
mkdir -p staticfiles
