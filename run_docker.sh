#!/usr/bin/env bash

docker build --build-arg PY_VERSION=${PY_VERSION} --build-arg SRC_DIR=${SRC_DIR} --build-arg REQUIREMENTS=${REQUIREMENTS} -t ${NAME} .
docker run -t ${NAME}
