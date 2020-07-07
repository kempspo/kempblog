### BUILDER
FROM python:3.7.6-buster as builder
LABEL maintainer="Kemp Po kempspo@gmail.com"

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y \
    libpq-dev \ 
    gcc \
    musl-dev \ 
    postgresql-contrib 

# lint
RUN pip install --upgrade pip
RUN pip install flake8
COPY . .
RUN flake8 --ignore=E501,F401 .

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

### FINAL
# pull official base image
FROM python:3.7.6-buster

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN groupadd app && useradd app -g app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafqiles
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME
COPY /media_cdn $APP_HOME/mediafiles
COPY /static_cdn $APP_HOME/staticfiles

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]