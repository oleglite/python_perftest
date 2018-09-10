#!/usr/bin/env bash

python 01_django_template.py && \
python 02_python_startup.py && \
python 03_json.py && \
python 04_ujson.py && \
python 05_regexp_v8.py && \
bash 06_django.sh &&
bash 07_django_uwsgi.sh
#bash 08_aiohttp.sh
#bash 09_sanic.sh

if [ $? -ne 0 ]
then
    echo "Failed"
    exit 1
fi
