FROM python:3.11.9-slim

WORKDIR /code

RUN pip install pika

COPY . .

CMD [ "python", "consumer.py" ]
