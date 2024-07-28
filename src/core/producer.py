import pika
from pika import BasicProperties


def send_message(message):
    # amqp_url = "amqp://rmuser:rmpassword@localhost:5672?connection_attempts=5&retry_delay=5"
    amqp_url = "amqp://rmuser:rmpassword@rabbit_mq:5672?connection_attempts=10&retry_delay=10"
    url_params = pika.URLParameters(amqp_url)
    connection = pika.BlockingConnection(url_params)

    queue = "flags"
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True)

    msg_props = pika.BasicProperties(delivery_mode=2)
    channel.basic_publish(exchange='', routing_key=queue, body=message, properties=msg_props)

    channel.close()
    connection.close()
