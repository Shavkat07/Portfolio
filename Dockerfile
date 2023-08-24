FROM python:3.10.12-alpine3.18
LABEL authors="shavkat"

COPY . /Portfolio
WORKDIR /Portfolio

COPY requirements.txt /Portfolio/requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

EXPOSE 8000


RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /Portfolio/requirements.txt

RUN adduser --disabled-password shavkat

USER shavkat












#FROM python:3.9
#
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#COPY . /TEST
#WORKDIR /TEST
#
#RUN pip install -r requirements.txt
#RUN chmod +x ./entrypoint.sh
#ENTRYPOINT ["./entrypoint.sh"]





