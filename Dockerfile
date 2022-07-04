FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/blog_api

COPY ./requirements.txt /usr/src/blog_api

RUN pip install -r /usr/src/blog_api/requirements.txt

COPY . /usr/src/blog_api