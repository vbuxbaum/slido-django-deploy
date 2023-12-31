#!/bin/bash

echo "Install dependencies"
export MYSQLCLIENT_CFLAGS=$(pkg-config mysqlclient --cflags) && export MYSQLCLIENT_LDFLAGS=$(pkg-config mysqlclient --libs) && apt install -y python3-dev default-libmysqlclient-dev build-essential pkg-config && pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput