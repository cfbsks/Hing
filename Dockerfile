FROM python:3.10-slim

WORKDIR /usr/src
ENV HOME /usr/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install curl -y \
    && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src

ENTRYPOINT ["python3", "hing.py"]