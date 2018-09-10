#!/usr/bin/env bash
set -x
mkdir -p logs
sh run27.sh > logs/run27_08.log
sh run36.sh > logs/run36_08.log
sh run37.sh > logs/run37_08.log
