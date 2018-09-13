#!/usr/bin/env bash

echo -e "\nCheck API..."
curl localhost:80 && \
curl localhost:80/record/read/5 && \
curl localhost:80/version | grep $1
if [ $? -eq 0 ]
then
    echo "APP $1 is ok"
else
    echo -e "\n\n\n"
    >&2 echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Invalid app version $1"
    echo -e "\n\n\n"
    echo "===================="
    ps aux
    echo "===================="
    exit 1
fi
