FROM python:3.6.9
#RUN python -m pip install --upgrade pip
RUN \
apt-get update -y && \
apt-get install python3 -y && \
apt-get install python3-pip -y && \
apt-get install vim -y

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python /app/app.py