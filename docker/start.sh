#!/bin/sh
set -e

echo "Waiting for DB..."

until pg_isready -h db -U user; do
  sleep 2
done

echo "Running migrations..."
alembic upgrade head

echo "Starting server..."
exec gunicorn \
  -k uvicorn.workers.UvicornWorker \
  app.main:app \
  -b 0.0.0.0:8000