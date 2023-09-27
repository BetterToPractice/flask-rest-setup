#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

export FLASK_APP=main.py
flask run --reload