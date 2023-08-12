FROM python:3.11-alpine AS base

RUN apk add gcc libc-dev

RUN pip install -U pip

FROM base AS builder

RUN pip install build twine

FROM base AS test
