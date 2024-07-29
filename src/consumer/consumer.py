import pika
from logger import logger
import time
import threading
from dotenv import load_dotenv
import os

load_dotenv()
RABBIT_LOGIN = os.environ.get("RABBIT_LOGIN")
RABBIT_PASSWORD = os.environ.get("RABBIT_PASSWORD")
RABBIT_HOST = os.environ.get("RABBIT_HOST")

amqp_url = f"amqp://{RABBIT_LOGIN}:{RABBIT_PASSWORD}@{RABBIT_HOST}:5672?connection_attempts=10&retry_delay=10"
url_params = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(url_params)

queue = "flags"
channel = connection.channel()
channel.queue_declare(queue=queue, durable=True)

def receive_message(ch, method, properties, body):
    # Если сообщение содержит "красный флаг", логировать эту информацию.
    if body.decode("utf-8")[-3:] == "red":
        logger.info(body.decode("utf-8"))

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue, on_message_callback=receive_message)
channel.start_consuming()
