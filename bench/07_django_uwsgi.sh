#!/usr/bin/env bash
cd django_app

uwsgi uwsgi.ini &
sleep 1

sh /home/src/wrk/check.sh django_app
if [ $? -ne 0 ]
then
    echo "Failed"
    exit 1
fi

echo -e "\nRun wrk..."
sh /home/src/wrk/run.sh

uwsgi --stop /run/uwsgi.pid
