# basic python image
FROM python:3.11

# declare the source directory
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# install pika to access rabbitmq
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

COPY ./src /code/src

CMD ["fastapi", "run", "app/main.py", "--port", "80"]
