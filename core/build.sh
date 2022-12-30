#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

python core/manage.py collectstatic --no-input
python core/manage.py migrate
python core/manage.py createsu  # new
