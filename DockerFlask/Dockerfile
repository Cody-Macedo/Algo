FROM python:3.6.9
RUN python -m pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "./site.py"]