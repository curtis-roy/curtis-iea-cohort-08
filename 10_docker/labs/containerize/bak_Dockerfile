# syntax=docker/dockerfile:1

FROM python:3.8-alpine

LABEL "maintainer"="marvin"

WORKDIR /app
RUN pip3 install Flask
COPY . .
EXPOSE 8080

ENV ENVIRONMENT=DEV
ENV DISPLAY_FONT=arial
ENV DISPLAY_COLOR=green

RUN addgroup -S appgroup && adduser -S -D marvin -G appgroup
USER marvin

#HEALTHCHECK
CMD python3 /app/app.py