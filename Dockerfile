FROM python:3.11-alpine

RUN apk add gcc libc-dev

RUN pip install -U pip

RUN pip install build twine

