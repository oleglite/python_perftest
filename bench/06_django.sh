#!/usr/bin/env bash
cd django_app
python run_ping.py
python run_post.py -p 3
python run_get.py -p 3
python run_post_get.py -p 3
