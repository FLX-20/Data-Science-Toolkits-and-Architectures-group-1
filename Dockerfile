FROM python:3.12-slim

RUN useradd -m appuser

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=10000000 --require-hashes -r requirements.txt

RUN chown -R appuser:appuser /app
USER appuser

COPY src /app/src

CMD ["python", "src/main.py", "--mode", "all"]
