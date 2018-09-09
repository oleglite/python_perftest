#!/usr/bin/env bash

cd django_app

echo -e "\nRun migrations..."
python manage.py migrate -v 0
python fill_in_records.py
