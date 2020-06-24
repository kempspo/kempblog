FROM python:3.7.6-buster
LABEL maintainer="Kemp Po kempspo@gmail.com"

RUN apt-get update && \
    apt-get install -y \
    libpq-dev \ 
    postgresql \
    postgresql-contrib 

WORKDIR /src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apt-get update && apt-get install -y python3.7.6 python3-pip
RUN pip install --upgrade pip
COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY . .