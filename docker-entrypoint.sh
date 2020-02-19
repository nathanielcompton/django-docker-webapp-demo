#!/bin/sh

# Before we can apply Django migraitons, we must wait for PostgreSQL to build.
if [ "$ENTRYPOINT_DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Once PostgreSQL has finished building, apply Django model migrations.
python ./manage.py flush --no-
python ./manage.py collectstatic
python ./manage.py migrate

exec "$@"
