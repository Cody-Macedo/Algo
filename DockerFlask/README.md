# Docker Flask
#### Own configuration
Ubuntu 18.04.5 LTS

###Docker install
Doc for the [installation on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

Doc for the [permission of docker. (Post-installation)](https://docs.docker.com/engine/install/ubuntu/)


### Images & Containers
Show images images : `docker images`  
show all containers (running ones) : `docker ps`  
show all containers : `docker ps -a`

### stop container
`docker stop "container"`
### remove all docker containers
`docker rm $(docker ps -aq)`
### remove all docker images 
`docker rmi $(docker images -q)`

###Dockerfile
Exemple Dockerfile (Python Flask):

Create your dependencies with `requirements.txt` (you can install it by your Dockerfile)  
For exemple add : `Flask==1.1.2`

Exemple of Dockerfile:  
`FROM python:3.6.9`  
`RUN python -m pip install --upgrade pip`  
`COPY . /app`  
`WORKDIR /app`  
`RUN pip install -r requirements.txt`  
`EXPOSE 5000`  
`CMD ["python3", "./site.py"]`  

Environment variables are supported by the following list of instructions in the Dockerfile:

* ADD  
* COPY
* ENV
* EXPOSE
* FROM
* LABEL
* STOPSIGNAL
* USER
* VOLUME
* WORKDIR
* ONBUILD

`build` make an image from the Dockerfile  
`run` creates a container from a given image and starts the container using a given command  
`exec` runs a new command in a running container.

**Published port**: When you create or run a container using docker create or docker run, it does not publish any of its ports to the outside world. To make a port available to services outside of Docker, or to Docker containers which are not connected to the container’s network, use the --publish or -p flag. This creates a firewall rule which maps a container port to a port on the Docker host to the outside world.
### build the image 
create the image
`docker build -t myapp:01 .`

### run container python flask

Run to instantiate the container  
`docker run --publish 5000:5000 --name myapp myapp:01`  

To make it background   
`docker run --publish 5000:5000 --detach myapp:01`  

Option:  
`-d` -> `--detach`  
`-b` -> `--publish`  
`docker run -d -p 5000:5000 myapp:01` 

### exec / Enter inside the container
`docker exec -it CONTAINER_ID /bin/bash`

###Heroku
running bash app:
`heroku run bash --app intense-savannah-03963`  
open (start web): 
`heroku open --app intense-savannah-03963`  
debug : 
`heroku logs --tail`