#!/usr/bin/env bash

export WRK=/home/wrk/wrk
cd /home/src/wrk

WRK_DURATION=60

export WRK_CONF="-c 1 -t 1 -d $WRK_DURATION --latency"
sh run_benches.sh

export WRK_CONF="-c 10 -t 1 -d $WRK_DURATION --latency"
sh run_benches.sh

export WRK_CONF="-c 100 -t 1 -d $WRK_DURATION --latency"
sh run_benches.sh
