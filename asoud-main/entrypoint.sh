#!/bin/sh

while ! nc -z db 5432 ; do
    echo "Waiting for the PostgreSQL Server"
    sleep 3
done

exec "$@"