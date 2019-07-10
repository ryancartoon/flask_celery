


## DB初始化

    flask db init
    flask db migrate
    flask db upgrade

## 启动开发环境服务

### 启动web server

    export FLASK_APP=manage.py
    export FLASK_ENV=development 
    flask run

### 启动redis-server

    redis-server

### 启动celery worker

    celery worker -A app.task.celery_app


### 访问Web API

    http://127.0.0.1:5000/api/home


#### 发起新任务

    http://127.0.0.1:5000/api/task/start

#### 查看所有的任务

    http://127.0.0.1:5000/api/tasks


## docker deploy

- build image

    docker build -f docker/Dockerfile -t app:latest .

- start service

    docker-compose -f docker/docker-compose.yaml up -d

- stop service

    docker-compose -f docker/docker-compose.yaml stop

- destroy service

    docker-compose -f docker/docker-compose.yaml rm

## TODO
- pytest
- coverage
