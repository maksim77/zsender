#!/bin/bash
while ! docker-machine env default
do
	docker-machine start default
done
eval $(docker-machine env default)
docker-compose down
docker-compose up -d
while ! nc -z $(docker-machine ip default) 10051
do
    sleep 1
done
