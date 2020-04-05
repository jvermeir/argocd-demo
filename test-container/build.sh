#!/usr/bin/env bash

git rev-parse --short HEAD > git-hash.txt
docker build . -t jvermeir/date-time
docker push jvermeir/date-time:latest