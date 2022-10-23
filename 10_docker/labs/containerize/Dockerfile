# syntax=docker/dockerfile:1

FROM python:3.8-alpine

LABEL "maintainer"="marvin"

WORKDIR /app
RUN pip3 install Flask
COPY . .
EXPOSE 8080

# TODO Set default values for env variables

# RUN addgroup -S appgroup
# RUN adduser -S -H -D marvin -G appgroup
# USER marvin

#HEALTHCHECK
CMD python3 /app/app.py