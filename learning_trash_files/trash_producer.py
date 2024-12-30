import pika
# import os

# read rabbitmq connection url from environment variable
# amqp_url = os.environ['localhost']
# amqp://rabbit_mq?connection_attempts=10&retry_delay=10
amqp_url = "http://localhost:5672?connection_attempts=3&retry_delay=1"
url_params = pika.URLParameters(amqp_url)

# connect to rabbitmq
connection = pika.BlockingConnection(url_params)
chan = connection.channel()

# declare a new queue
# durable flag is set so that messages are retained
# in the rabbitmq volume even between restarts
chan.queue_declare(queue='hello', durable=True)

# publish a 100 messages to the queue
for i in range(100):
    chan.basic_publish(exchange='', routing_key='hello',
                       body='Hello World', properties=pika.BasicProperties(delivery_mode=2))
    print("Produced the message")

# close the channel and connection
# to avoid program from entering with any lingering
# message in the queue cache
chan.close()
connection.close()
