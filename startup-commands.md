# Startup Commands

This is a reference for docker startup commands.
Webserver for frontend, python flask running for backend, mongo running as database.
See relevant sections below.

## Run

### Network

docker network create --driver bridge thingnet

### Frontend

docker build --tag react .
docker run -ditp 3000:3000 --network thingnet --rm --name frontend react

### Backend

docker build --tag flask .
docker run -ditp 5000:5000 --env-file .env --rm --network thingnet --name backend flask

### Mongo

docker run -dit --network thingnet --rm --name db mongo:latest

## Volume

docker volume create mountain

## Compose

docker compose up -d

docker compose down

# Verify data
docker exec -ti character-creation-backend-db-1 sh
mongo
use app
db.character_sheets.find()

