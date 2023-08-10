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
- volume
- exposition port
- architecture

## Starting

1. Run code in local without docker
```bash
uvicorn main:app --reload
```
