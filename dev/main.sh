#!/bin/bash

set -e

cd `dirname $0`
source _util

erun pip install -r requirements.txt
erun rm -Rf $PWD
