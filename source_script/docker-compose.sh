#!/bin/bash
#
# このスクリプト中の関数は全て
# カレントディレクトリがリポジトリのルートディレクトリの状態で呼び出されることと、
# source_script/utilをsourceしていることを前提としている。

set -e

if [ ${#REGISTRY} -ne 0 ]; then
  if [ ${#D_USER} -ne 0 ]; then
    IMAGE_PATH=$REGISTRY/$D_USER/$IMAGE
  else
    IMAGE_PATH=$REGISTRY/$IMAGE
  fi
else
  if [ ${#D_USER} -ne 0 ]; then
    IMAGE_PATH=$D_USER/$IMAGE
  else
    IMAGE_PATH=$IMAGE
  fi
fi

BASE_NAME=`basename $PWD`

default_service_name() {
  echo `basename $PWD`
}

build() {
  # docker build
  if [ $# -ne 1 ]; then
    echo "Usage: build <TAG>"
    exit 1
  fi

  check_ap_env

  TAG=$1
  DOCKER_FILE=${DOCKER_FILE:-Dockerfile}
  ENV_NAME=${DOCKER_FILE:-$BASE_NAME}

  erun docker build -f $ENV_NAME/Dockerfile -t $IMAGE_PATH:${ENV_NAME}-$TAG .
}
