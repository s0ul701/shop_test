# Shop (test project)

This file describes all the steps to create and run `Shop` application.

## Local development

### First start commands

`$ docker-compose build`

`$ docker-compose up`

`$ fab migrate`

### Access

* http://localhost:8000

### Fabric

`fabfile.py` сontains some functions usefull for local development.

#### Setup

    `$ sudo pip install fabric3`

#### Main commands

    `$ fab makemigrations`

    `$ fab migrate`

    `$ fab createsuperuser`

    `$ fab сollectstatic`

    `$ fab test`

## API description

API-url: `/api/v1/

API endpoints:
* `users/`
* `products/`
* `invoices/`
* `token/`
* `token-refresh/`