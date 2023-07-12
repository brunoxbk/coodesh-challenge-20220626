#!/bin/sh

if [ "$DEFAULT_DB_ENGINE" = "postgis" ] || [ "$DEFAULT_DB_ENGINE" = "postgres" ]
then
echo "Waiting for postgres..."

    while ! nc -z db $DEFAULT_DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"

fi
python manage.py migrate --noinput
echo "run migrations"

if [ "$DEBUG" = "False" ]
then
python manage.py collectstatic --noinput
echo "colleted static files"

exec gunicorn core.wsgi:application --bind ${RUN_HOST}:${RUN_PORT}
else
  exec python manage.py runserver ${RUN_HOST}:${RUN_PORT}
fi
