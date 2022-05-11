FROM python:3.10-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir /app
WORKDIR /app

RUN apt-get update
RUN apt-get install -y libgdal-dev
RUN pip install --upgrade pip
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
