#!/bin/bash

pip install -r requirements.txt
python manage.py migrate
gunicorn --bind 0.0.0.0:8000 sekura.asgi:application -k uvicorn.workers.UvicornWorker