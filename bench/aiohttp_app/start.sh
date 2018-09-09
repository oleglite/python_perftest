#!/usr/bin/env bash

echo -e "start"


for i in {1..4}; do
    python app.py --path=/tmp/aiohttp_app_${i}.sock &
done


cp nginx.conf /etc/nginx/nginx.conf
nginx
