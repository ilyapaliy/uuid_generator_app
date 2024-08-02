import logging
from aio_pika import connect_robust, Message
import os
from dotenv import load_dotenv
from schemas import XFlag


load_dotenv()
RABBIT_LOGIN = os.environ.get("RABBIT_LOGIN")
RABBIT_PASSWORD = os.environ.get("RABBIT_PASSWORD")
RABBIT_HOST = os.environ.get("RABBIT_HOST")

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class PikaConsumer:
	async def consume(self, loop):
		self.connection = await connect_robust(
			host=RABBIT_HOST,
			port=5672,
			login=RABBIT_LOGIN,
			password=RABBIT_PASSWORD,
			virtual_host="/",
			loop=loop
		)
		self.channel = await self.connection.channel()
		queue = await self.channel.declare_queue(name="flags", durable=True)
		await queue.consume(self.process_incoming_message, no_ack=False)
		logger.info("Established PikaConsumer connection")
		return self.connection

	async def process_incoming_message(self, message):
		if message.body.decode()[-9:] == str(XFlag.red):
			logger.info(message.body.decode())
		await message.ack()

	async def close_connection(self):
		await self.channel.close()
		await self.connection.close()
		logger.info("PikaConsumer connection closed")
