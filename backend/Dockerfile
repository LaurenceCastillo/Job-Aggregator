FROM python:3.11-slim
 
WORKDIR /backend
 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
 
# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat-openbsd gcc postgresql \
  && apt-get clean
 
# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt
 
COPY . /backend
 