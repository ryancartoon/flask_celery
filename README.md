# Flask Celery集成


## 安装项目依赖

    python -m venv venv; source venv/bin/activate
    pip install -r requirements.txt
    pip install --upgrade https://github.com/jakubroztocil/httpie/archive/master.tar.gz


## 启动开发环境服务

### export flask env

    export FLASK_APP=manage.py
    export FLASK_ENV=development 


### DB初始化

在初始化前，需要先删除掉db文件和migrations文件夹。

    flask db init
    flask db migrate
    flask db upgrade


### 启动web server

    flask run


### 启动redis-server

    redis-server

### 启动celery worker

    celery worker -A app.task.celery_app


#### 发起新任务

    http post http://127.0.0.1:5000/api/tasks

#### 查看所有的任务

    http http://127.0.0.1:5000/api/tasks


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
