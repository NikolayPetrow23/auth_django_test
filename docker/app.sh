#!/bin/bash
python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --noinput

cp -r /app/static . /app/static/

gunicorn --bind 0.0.0.0:9000 auth_django_test.wsgi
