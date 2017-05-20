# docker-app-example

## Requirements

* yarn
* direnv
* Docker Engine
* Docker Compose

## Setup

Run `setup` command to install npm modules and run docker containers.

```
$ setup
```

```
$ watch
```

## build and push docker images for specific enviroment (development, staging, production, etc)

```
$ cd dev
$ images  # docker images
$ build 1.0.0  # docker build
$ vi docker-compose.yml
$ run  # docker-compose up -d
$ dps  # docker-compose ps
$ logs -f  # docker-compose logs -f ap
$ stop  # docker-compose stop
$ push 1.0.0  # docker push
$ drm  # docker-compose rm
```
