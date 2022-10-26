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

USER 1000

HEALTHCHECK --interval=15s --timeout=3s \
  CMD ping -s 2 -c 2 -q 127.0.0.1:8080 || exit 1

CMD python3 /app/app.py