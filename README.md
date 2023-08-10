# Initiation Docker 

## Objectifs
- comprendre rapidement la containerization : https://algodaily.com/lessons/what-is-a-container-a-docker-tutorial
- utilisation de docker-compose
- récupérer une image docker depuis docker hup
- créer une image docker, et la pusher sur dockerhub
- mettre une API sur docker, et l'utiliser en local

## Prérequis
- avoir installer docker et docker compose
pour vérifier : 
```bash
docker -v
docker-compose -v
```
run the hello world image
```bash
docker run hello-world
```
## Vocabulaire
- image
- contenaire
- container registry
- volume
- exposition port
- architecture

## Starting

1. A executer avec un virtual env
```bash
uvicorn main:app --reload
```

## Useful commands for docker
play arround with image python:3.10 (https://hub.docker.com/layers/library/python/3.10/images/sha256-527cc6f230cf7de1f972fbb0ffc850035e91fb4a52058b44906ea706b3018bb6?context=explore)

download the image
```bash
docker pull <name>
```

```bash
docker build -t <name> .
```

```bash
docker run -p 8000:800 <name>
```
To go inside a container
```bash
docker run -it <name>
```

```bash

## Useful commands for docker compose

permets de build et de runner en une seule command
```bash
docker-compose up --build
```

```bash
docker-compose exec <id|name> bash
```