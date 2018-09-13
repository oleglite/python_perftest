#!/usr/bin/env bash
cd aiohttp_app
sleep 5 && ps aux

bash start.sh &
sleep 5


bash /home/src/wrk/check.sh aiohttp_app
if [ $? -ne 0 ]
then
    echo "Failed"
    exit 1
fi

echo -e "\nRun wrk..."
bash /home/src/wrk/run.sh
bash stop.sh
