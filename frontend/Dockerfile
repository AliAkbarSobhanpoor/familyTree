# frontend/Dockerfile
FROM node:20-alpine as build

WORKDIR /app

# Install dependencies
COPY ./package*.json ./
RUN npm install

# Copy and build
COPY . .
RUN npm run build
