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

CMD python3 /app/app.py

HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhosed/ || exit 1