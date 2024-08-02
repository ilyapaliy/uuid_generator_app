### This project is a test task for compeny othercode.

Solution is API built with framework FastAPI.

Required:

python 3.11
[direct link](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe)

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

Run

```shell
docker-compose up --build
```

in rabbitmq folder to start RabbitMQ service from docker.

* login: rmuser
* password: rmpassword

### Starting development environment

1. Enshure that you're using console with enabled virtual env
2. Enshure that RabbitMQ is running
3. Use "python src/main.py" command to start server

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
