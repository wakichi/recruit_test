#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
cd django_rest_framework
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py newsuperuser