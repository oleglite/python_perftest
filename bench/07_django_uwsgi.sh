#!/usr/bin/env bash
cd django_app

uwsgi uwsgi.ini &
sleep 1


echo -e "\nCheck API..."
curl localhost:8080
curl localhost:8080/record/read/5

echo -e "\nRun wrk..."
sh /home/src/wrk/run.sh
