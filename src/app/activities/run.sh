#!/bin/bash
set -e
pip install -r /app/activities/requirements.txt
cd /app/activities/activities && gunicorn --reload -b 0.0.0.0:8000 app:app
