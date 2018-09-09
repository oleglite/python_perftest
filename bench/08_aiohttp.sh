#!/usr/bin/env bash
cd aiohttp_app

bash start.sh &
sleep 1


echo -e "\nCheck API..."
curl -v localhost
curl -v localhost/record/read/5

echo -e "\nRun wrk..."
bash /home/src/wrk/run.sh
