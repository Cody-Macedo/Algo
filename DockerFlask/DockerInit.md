# Docker Flask

### Images & Containers
Show images images : `docker images`  
show all containers (running one) : `docker ps`  
show all containers : `docker ps -a`

### stop container
`docker stop "container"`
### remove all docker containers
`docker rm $(docker ps -aq)`
### remove all docker images 
`docker rmi $(docker images -q)`

### run container python flask
`docker run --publish 5000:5000 --name miniapp python-miniapp:01`

`docker run --publish 5000:5000 --detach python-miniapp:01`

`docker run -d -p 5000:5000 python-miniapp:01`


###Dockerfile
Exemple Dockerfile (Python Flask):

Freate your dependencies in `requirements.txt`  
For exemple add : `Flask==1.1.2`

`FROM python:3.6.9`  
`RUN python -m pip install --upgrade pip`  
`COPY . /app`  
`WORKDIR /app`  
`RUN pip install -r requirements.txt`  
`EXPOSE 5000`  
`CMD ["python3", "./site.py"]`  
