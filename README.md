# flask_celery

flask and celery integration


## start flask

    export FLASK_APP='manage.py'
    flask run


## start celery

    celery worker -A app.task.celery_app


## TODO
- add sqlalchemy
