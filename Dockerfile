FROM python:3.10-slim

MAINTAINER "sa5mchavez"


WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
EXPOSE 3306 5000
CMD ["python", "app.py"]