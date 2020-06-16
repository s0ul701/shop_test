FROM python:3.8-slim

RUN mkdir /server

WORKDIR /server

COPY server/requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
