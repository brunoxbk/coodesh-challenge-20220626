# Backend Challenge 20220626

Desenvolvimento de uma REST API com os dados do projeto Open Food Facts raspados via crawler

# Stack

 - Docker
 - Python/Django
 - PostgreSQL
 - Scrapy
 - Celery
 - Django REST Framework
 
 # Variáveis de ambiente .env

    DEBUG=True
    SECRET_KEY=arandomstring
    ALLOWED_HOSTS=*,
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=db
    DB_PORT=5432
    CACHE_BACKEND=django_redis.cache.RedisCache
    CACHE_LOCATION=redis://cache:6379/0
    CACHE_CLIENT_CLASS=django_redis.client.DefaultClient
    RUN_PORT=8000
    RUN_HOST=0.0.0.0

# Comandos
    docker compose build
    docker compose up

> This is a challenge by [Coodesh](coodesh.com)`