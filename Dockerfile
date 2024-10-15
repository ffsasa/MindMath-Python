FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    libgirepository1.0-dev \
    pkg-config \
    libcairo2-dev \
    libpango1.0-dev \
    python3-dev \
    ffmpeg \
    && apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python3", "main.py"]
