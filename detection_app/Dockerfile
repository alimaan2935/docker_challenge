FROM tiangolo/uwsgi-nginx-flask:python3.7
LABEL maintainer="alimaan2935@hotmail.com"
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
