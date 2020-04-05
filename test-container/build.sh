#!/usr/bin/env bash

docker build . -t jvermeir/date-time
docker push jvermeir/date-time:latest