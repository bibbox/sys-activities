FROM python:2.7-slim
MAINTAINER  lomadi <lomadi@mac.com>

RUN pip install --upgrade pip

COPY . /requirements
WORKDIR /requirements
# install requirements
RUN pip install -r requirements.txt
EXPOSE 8000

