FROM ubuntu:16.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	git \
	sqlite3 \
	curl \
	make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev


RUN curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

ARG PY_VERSION
RUN /root/.pyenv/bin/pyenv install $PY_VERSION
RUN rm -rf /var/lib/apt/lists/*
ENV PATH "/root/.pyenv/versions/$PY_VERSION/bin/:${PATH}"

ARG REQUIREMENTS
COPY $REQUIREMENTS /home/src/requirements.txt
RUN pip install -r /home/src/requirements.txt

# add (the rest of) our code
ARG SRC_DIR
COPY $SRC_DIR /home/src/

WORKDIR /home/src/
ENTRYPOINT /home/src/run.sh
