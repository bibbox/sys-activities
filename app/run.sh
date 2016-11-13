#!/bin/bash
set -e
pip install -r /app/requirements.txt
cd /app/activities/ && gunicorn --reload -b 0.0.0.0:8000 app:app
