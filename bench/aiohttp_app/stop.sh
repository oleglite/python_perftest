#!/usr/bin/env bash

echo -e "stop"

nginx -s quit
rm /etc/nginx/nginx.conf


ps aux
kill $(ps aux | grep '[p]ython app.py' | awk '{print $2}')
sleep 5
ps aux
