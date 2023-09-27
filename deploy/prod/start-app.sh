#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

export FLASK_APP=main.py
flask run -w 4 --host 0.0.0.0 --port 5000 --reload