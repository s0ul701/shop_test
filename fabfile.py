import os

from fabric.api import local


def makemigrations(app=''):
    local(
        "docker-compose up --build -d  && \
        docker exec -it $(docker ps | grep shop_server | awk '{{ print $1 }}') python manage.py makemigrations {} && \
        docker-compose stop".format(app)
    )


def migrate(app=''):
    local(
        "docker-compose up --build -d  && \
        docker exec -it $(docker ps | grep shop_server | awk '{{ print $1 }}') python manage.py migrate {} && \
        docker-compose stop".format(app)
    )


def createsuperuser():
    local(
        "docker-compose up --build -d  && \
        docker exec -it $(docker ps | grep shop_server | awk '{{ print $1 }}') python manage.py createsuperuser && \
        docker-compose stop"
    )


def collectstatic():
    local(
        "docker-compose up --build -d  && \
        docker exec -it $(docker ps | grep shop_server | awk '{{ print $1 }}') python manage.py collectstatic && \
        docker-compose stop"
    )


def test(path=''):
    local(
        "docker-compose up --build -d  && \
        docker exec -it $(docker ps | grep shop_server | awk '{{ print $1 }}') python manage.py test {} && \
        docker-compose stop".format(path)
    )
