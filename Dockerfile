FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080 \
    APP_DATA_DIR=/data

WORKDIR /app

COPY index.html server.py properties.json ./

RUN mkdir -p /data

EXPOSE 8080

CMD ["python3", "server.py"]
