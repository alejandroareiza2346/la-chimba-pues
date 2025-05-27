#!/bin/bash
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
cp -r static/* staticfiles/
cp -r staticfiles/* static/
