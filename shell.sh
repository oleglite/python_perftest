#!/usr/bin/env bash

PY_VERSION=3.7.0
NAME=py37
SRC_DIR=bench
REQUIREMENTS=./requirements/3.7.0.txt

docker build --build-arg PY_VERSION=${PY_VERSION} --build-arg SRC_DIR=${SRC_DIR} --build-arg REQUIREMENTS=${REQUIREMENTS} -t ${NAME} .
docker run --entrypoint /bin/bash -it ${NAME}
