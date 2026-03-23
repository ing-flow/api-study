FROM python:3.12-slim

WORKDIR /app

# 必要パッケージ
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコピー
# COPY . .
COPY app ./app
COPY alembic ./alembic
COPY alembic.ini .
COPY app.py .

# ポート
EXPOSE 8000

# 起動
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "-b", "0.0.0.0:8000"]