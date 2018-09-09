#!/usr/bin/env bash

printf "\nWRK PING BENCH:\n"
printf "==========================================\n"
$WRK $WRK_CONF http://localhost:80

printf "\nWRK GET BENCH:\n"
printf "==========================================\n"
$WRK $WRK_CONF -s /home/src/wrk/read.lua http://localhost:80
