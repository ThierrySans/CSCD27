#!/bin/bash

docker stop $(docker ps -a -q)
docker rm -f $(docker ps -a -q)
docker network rm $(docker network ls -q)
docker volume rm $(docker volume ls -f dangling=true -q)
docker rmi $(docker images -f dangling=true -q)