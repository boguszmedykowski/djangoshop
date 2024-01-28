# Etap 1: Budowanie aplikacji
FROM node:latest
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

ARG VUE_APP_API_URL
ENV VUE_APP_API_URL=$VUE_APP_API_URL
COPY .env .env

RUN npm run build

RUN npm install -g http-server
EXPOSE 8080
CMD ["http-server", "dist"]
