#!/bin/bash

python3 docker_clean.py
docker image ls -q | docker image rm $(</dev/stdin) --force
docker container ls -q | docker container rm $(</dev/stdin) --force
