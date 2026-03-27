#!/bin/sh

alembic upgrade head

exec gunicorn \
  -k uvicorn.workers.UvicornWorker \
  app.main:app \
  -b 0.0.0.0:8000