FROM python:3.12-slim

WORKDIR /app

# 必要パッケージ
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコピー
COPY . .

# ポート
EXPOSE 8000

# 起動
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]