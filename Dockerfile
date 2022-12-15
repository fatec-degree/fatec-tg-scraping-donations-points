FROM python:3.8.10-slim
WORKDIR /app
COPY src src
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
