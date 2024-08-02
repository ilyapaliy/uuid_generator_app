from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import asyncio
import logging
from contextlib import asynccontextmanager
import routs
from pika_consumer import PikaConsumer
from pika_producer import PikaProducer


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pika_producer = PikaProducer()
        self.pika_consumer = PikaConsumer()


@asynccontextmanager
async def lifespan(app: App):
    loop = asyncio.get_running_loop()
    consumer_task = loop.create_task(app.pika_consumer.consume(loop))
    producer_task = loop.create_task(app.pika_producer.connect(loop))
    await consumer_task
    await producer_task
    yield
    await loop.create_task(app.pika_consumer.close_connection())
    await loop.create_task(app.pika_producer.close_connection())


app = App(
	title="Get UUID",
	docs_url="/api/docs",
	openapi_url="/api/openapi.json",
	lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://0.0.0.0:80",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(routs.router)


if __name__ == "__main__":
    uvicorn.run(
    	app="main:app",
    	host="127.0.0.1",
    	port=8000,
    	reload=True,
    	reload_excludes="*.log"
    )
