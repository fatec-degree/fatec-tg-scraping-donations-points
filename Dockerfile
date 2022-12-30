FROM python:3.8-slim

ENV DB_HOST=$DB_HOST \
    DB_USER=$DB_USER \
    DB_PASSWORD=$DB_PASSWORD \
    DB_NAME=$DB_NAME \
    MAPS_API_KEY=$MAPS_API_KEY \
    ENVIRONMENT=$ENVIRONMENT \
    ADDRESS_API_URL=$ADDRESS_API_URL

WORKDIR /app

RUN apt update && apt upgrade && \
    apt install curl -y && \
    apt install unzip -y && \
    apt install gnupg -y && \
    CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver && \
    curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get -yqq update && \
    apt-get -yqq install google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD google-chrome-stable --no-sandbox --headless && python3 src/main.py
