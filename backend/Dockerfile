# backend/Dockerfile
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libcairo2 \
    libcairo2-dev \
    libjpeg-dev \
    libpng-dev \
    libffi-dev \
    libpango1.0-dev \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*
# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
    
# Copy the rest of the backend code
COPY . .