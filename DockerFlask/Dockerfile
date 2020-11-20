FROM python3:3.6.9
RUN python -m pip install --upgrade pip
COPY . /app
RUN pip freeze > requirements.txt
RUN python -m pip install -r requirements.txt
EXPOSE 5000
CMD python3 site.py

# arreter un container
# docker stop container
# all docker container remove
# docker rm $(docker ps -aq)
# all docker images remove
# docker rmi $(docker images -q)

#docker run --publish 5000:5000 --name miniapp python-miniapp:01
