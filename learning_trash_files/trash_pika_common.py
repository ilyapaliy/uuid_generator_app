from contextlib import contextmanager
from pika import BlockingConnection, PlainCredentials, ConnectionParameters


@contextmanager
def get_channel(queue: str) -> BlockingConnection:
    credentials = PlainCredentials('user', 'bitnami')
    config = ConnectionParameters(host='localhost', credentials=credentials)
    connection = BlockingConnection(config)
    channel = connection.channel()
    channel.queue_declare(queue=queue,
                          durable=True,
                          arguments={'x-max-priority': 10})
    try:
        yield channel
    finally:
        if connection is not None:
            connection.close()
            print('Connection closed.')