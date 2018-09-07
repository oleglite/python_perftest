#!/usr/bin/env bash

export IN_MEMORY_DB=1

PERF_CONF="--stats --inherit-environ=IN_MEMORY_DB"

cd django_app
python run_ping.py $PERF_CONF
python run_post.py $PERF_CONF -p 3
python run_get.py $PERF_CONF -p 3
python run_post_get.py $PERF_CONF -p 3
