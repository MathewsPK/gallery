#!/bin/bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata birds_fixture.json
python manage.py collectstatic --noinput
