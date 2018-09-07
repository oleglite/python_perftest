#!/usr/bin/env bash

export WRK=/home/wrk/wrk
cd /home/src/wrk

export WRK_CONF="-c 1 -t 1 -d 30 --latency"
sh run_benches.sh

export WRK_CONF="-c 60 -t 4 -d 30 --latency"
sh run_benches.sh
