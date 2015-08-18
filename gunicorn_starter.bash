#!/bin/bash
# For use with Docker
cd /challengeboard
export DATA_DIR=/data/
python3 manage.py migrate
gunicorn \
	-b '0.0.0.0:80' \
	-w 3 --max-requests 1000 --max-requests-jitter 50 \
	challengeboard.wsgi
