#!/usr/bin/env bash

set -e

source "$APP_HOME/venv/bin/activate"

cd $APP_HOME/flask_celery

case $1 in
    web)
    gunicorn manage:app -b 0.0.0.0:$web_port;;

    worker)
    celery worker -A app.task.celery_app;;

    beat)
    celery beat -A app.task.celery_app;;
esac

exec "$@"
