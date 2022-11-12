#!/bin/bash

pip install -r requirements.txt
python manage.py makemigrations
python manage.py collectstatic --no-input
chown -R 1000:1000 *
python manage.py migrate
