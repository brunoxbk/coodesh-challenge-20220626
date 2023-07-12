FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y --no-install-recommends \
    libgdal-dev \
    python3-dev \
    libpq-dev \
    netcat \
    g++ \
    gcc && \
    pip install numpy==1.18.1 && \
    pip install gdal==2.4.0 && \
    apt remove -y gcc g++ && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
COPY entrypoint.sh /code/

RUN chmod +x /code/entrypoint.sh

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . /code/

RUN chmod +x /code/entrypoint.sh
