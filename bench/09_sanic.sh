#!/usr/bin/env bash
cd sanic_app
sleep 5 && ps aux

bash start.sh &
sleep 1


bash /home/src/wrk/check.sh sanic_app
if [ $? -ne 0 ]
then
    echo "Failed"
    exit 1
fi

echo -e "\nRun wrk..."
bash /home/src/wrk/run.sh
bash stop.sh
