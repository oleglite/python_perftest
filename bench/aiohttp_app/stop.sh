#!/usr/bin/env bash

echo -e "stop"

nginx -s quit
rm /etc/nginx/nginx.conf

kill -9 $(ps aux | grep '[p]ython app.py' | awk '{print $2}')
