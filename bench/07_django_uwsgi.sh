#!/usr/bin/env bash
cd django_app

echo -e "\nRun migrations..."
python manage.py migrate -v 0
python fill_in_records.py

uwsgi uwsgi.ini &
sleep 1


echo -e "\nCheck API..."
curl localhost:8080
curl localhost:8080/record/read/5

echo -e "\nRun wrk..."
sh /home/src/wrk/run.sh
