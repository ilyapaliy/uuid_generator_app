import pika
from pika import BasicProperties


def send_message(message):
    amqp_url = "http://localhost:5672?connection_attempts=5&retry_delay=5"
    url_params = pika.URLParameters(amqp_url)
    connection = pika.BlockingConnection(url_params)

    queue = "flags"
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True)

    msg_props = pika.BasicProperties(delivery_mode=2)
    channel.basic_publish(exchange='', routing_key=queue, body=message, properties=msg_props)

    channel.close()
    connection.close()
