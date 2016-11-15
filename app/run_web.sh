#!/bin/bash
set -e
cd /app/activities/ && gunicorn --reload -b 0.0.0.0:8000 app:app
