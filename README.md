### This project is a test task for compeny othercode.

Solution is API built with framework FastAPI.

Required:

1. python 3.11
[direct link](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe)
2. RabbitMQ 3.13.4
[direct link](https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.13.4/rabbitmq-server-3.13.4.exe)
3. Erlang 26.2.5.2
[direct link](https://github.com/erlang/otp/releases/download/OTP-26.2.5.2/otp_win64_26.2.5.2.exe)

Project can be deployed in two ways:

1. In docker
2. For development

In both cases first should be done some preparations:

### Virtual env

Create virtual env

```shell
python -m venv env
```

Activate virtual enviroment and install required packets

```shell
./env/Scripts/Activate.ps1
pip install -r requirements.txt
```

(or use other activate script in the same folder)

Use this command to exit virtual environment

```shell
deactivate
```

### RabbitMQ

Comand to enable RabbitMQ GUI by [link](http://127.0.0.1:15672/)

```shell
rabbitmq-plugins enable rabbitmq_management
```

* default login: guest
* default password: guest

Other useful commands

```shell
rabbitmqctl help
rabbitmqctl status
rabbitmqctl shutdown
rabbitmqctl start_app
```

### Starting development environment

1. Enshure that you're using console with enabled virtual env
2. Enshure that RabbitMQ is running
3. Use "python src/main.py" command to start server
4. Open another terminal, enable virtual env and use "python src/consumer.py" to start consumer

All done! Now you can use Postman or other program to check it out.

### Testing

Run this comand with enabled virtual env

```shell
pytest -v tests/
```

### Creating docker containers

```shell
docker-compose up
```

### Docs

Api swagger docs located on [address](http://localhost:8000/api/docs)
