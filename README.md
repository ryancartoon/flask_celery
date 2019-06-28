
## docker deploy
build image
```bash
docker build -f docker/Dockerfile -t app:latest .
```

start service
```bash
docker-compose -f docker/docker-compose.yaml up -d
```

stop service
```bash
docker-compose -f docker/docker-compose.yaml stop
```

destroy service
```bash
docker-compose -f docker/docker-compose.yaml rm
```

## TODO
- add sqlalchemy
