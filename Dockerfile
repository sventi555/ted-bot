FROM python:3.7

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libnss3 

RUN pip install pipenv

# chromedriver
RUN wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin/chromedriver
ENV CHROME_LOCATION /usr/bin/chromedriver

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

RUN mkdir /app
WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --deploy

COPY . .

CMD ["pipenv", "run", "python", "script.py"]




