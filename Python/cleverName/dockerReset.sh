#! /bin/bash

docker-compose down
docker rmi $(docker images -aq)
docker-compose up -d
ssh-keygen -R 172.16.10.10
