# syntax=docker/dockerfile:1

FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8080

CMD python3 /app/app.py