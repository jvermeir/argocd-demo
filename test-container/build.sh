#!/usr/bin/env bash

if [ $# -lt 1 ]; then
    echo "Usage: ./build.sh <version>"
    exit -1
fi
echo $1
VERSION=$1

git rev-parse --short HEAD > git-hash.txt
docker build . -t jvermeir/date-time:$VERSION
docker push jvermeir/date-time $VERSION

rm git-hash.txt
