FROM python:3.12-slim

RUN useradd -m appuser

WORKDIR /app

RUN pip install --upgrade pip

COPY . .
RUN pip install --no-cache-dir --default-timeout=10000000 -r requirements.txt

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:create_app()"]
