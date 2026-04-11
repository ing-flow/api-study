FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 必要パッケージ
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコピー
# COPY . .
COPY app ./app
COPY alembic ./alembic
COPY alembic.ini .

# ポート
EXPOSE 8000

# 起動
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "-b", "0.0.0.0:8000"]
COPY docker/start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
