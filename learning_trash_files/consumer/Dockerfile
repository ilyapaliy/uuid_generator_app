FROM python:3.11.9-slim

WORKDIR /code

RUN pip install pika==1.3.2 python-dotenv==1.0.1

COPY . .

CMD [ "python", "consumer.py" ]
