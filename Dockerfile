FROM python:3.10.4-alpine3.14
LABEL version="1.0.0"
MAINTAINER Apisod.com

ENV PYTHONBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code/

# COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

