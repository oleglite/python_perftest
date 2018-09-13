#!/usr/bin/env bash
set -x
mkdir -p logs
sh run27.sh | tee logs/run27.log
sh run36.sh | tee logs/run36.log
sh run37.sh | tee logs/run37.log
