#!/bin/bash

pip install -r requirements.txt
python manage.py migrate
#gunicorn --bind 0.0.0.0:8000 sekura.asgi -k uvicorn.workers.UvicornWorker --reload
#gunicorn --bind 0.0.0.0:8000 sekura.asgi --reload
python manage.py runserver 0.0.0.0:8000
