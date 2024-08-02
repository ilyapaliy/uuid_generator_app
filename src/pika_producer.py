import logging
from aio_pika import connect_robust, Message
import os
from dotenv import load_dotenv


load_dotenv()
RABBIT_LOGIN = os.environ.get("RABBIT_LOGIN")
RABBIT_PASSWORD = os.environ.get("RABBIT_PASSWORD")
RABBIT_HOST = os.environ.get("RABBIT_HOST")

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class PikaProducer:
	def __init__(self):
		self.queue = "flags"
		
	async def connect(self, loop):
		self.connection = await connect_robust(
			host=RABBIT_HOST,
			port=5672,
			login=RABBIT_LOGIN,
			password=RABBIT_PASSWORD,
			virtual_host="/",
			loop=loop
		)
		self.channel = await self.connection.channel()
		await self.channel.declare_queue(name=self.queue, durable=True)
		logger.info("Established PikaProducer connection")
		return self.connection

	async def send_message(self, message: str):
		msg = Message(body=message.encode())
		await self.channel.default_exchange.publish(
			msg, routing_key=self.queue,
		)

	async def close_connection(self):
		await self.channel.close()
		await self.connection.close()
		logger.info("PikaProducer connection closed")
