import pika
from pika import BasicProperties
from dotenv import load_dotenv
import os


load_dotenv()
RABBIT_LOGIN = os.environ.get("RABBIT_LOGIN")
RABBIT_PASSWORD = os.environ.get("RABBIT_PASSWORD")
RABBIT_HOST = os.environ.get("RABBIT_HOST")


def send_message(message):
    amqp_url = f"amqp://{RABBIT_LOGIN}:{RABBIT_PASSWORD}@{RABBIT_HOST}:5672?connection_attempts=10&retry_delay=10"
    url_params = pika.URLParameters(amqp_url)
    connection = pika.BlockingConnection(url_params)

    queue = "flags"
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True)

    msg_props = pika.BasicProperties(delivery_mode=2)
    channel.basic_publish(exchange='', routing_key=queue, body=message, properties=msg_props)

    channel.close()
    connection.close()
