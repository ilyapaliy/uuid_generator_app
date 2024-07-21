# basic python image
FROM python:3.11

# install pika to access rabbitmq
RUN pip install pika

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

# declare the source directory
WORKDIR /code/src

# copy the file
COPY consumer.py /code/src

# start command
CMD [ "python", "/code/src/consumer.py" ]
