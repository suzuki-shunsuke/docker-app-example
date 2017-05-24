#!/bin/bash

set -e

erun() {
  # 実行するコマンドを標準出力してから実行
  echo "===================="
  echo "+ $@"
  echo "===================="
  "$@"
}

check_ap_env() {
  # AP_ENVが定義されていなかったら終了させる
  if [ ${#AP_ENV} -eq 0 ]; then
    echo "AP_ENV is not defined!"
    exit 1
  fi
}
