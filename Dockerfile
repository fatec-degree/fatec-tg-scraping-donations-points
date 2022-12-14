FROM python:3.8.10
COPY src /app/src
COPY requirements.txt /app
RUN cd /app && pip install --upgrade pip && pip install -r requirements.txt lint
ENTRYPOINT ["tail", "-f", "/dev/null"]
