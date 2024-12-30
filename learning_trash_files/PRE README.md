TODOs file:

Docker container starts with many connection errors just because long RabbitMQ start
Logging info model may be put in schemas for consistency.
Schemas may be used in tests.
Fixture RabbitMQ queue name.
Not tested on real server.
Not tested SSL.

Паралельные тесты:
pip install pytest-xdist
pytest -v -n5 tests/

git ls-files | xargs wc -l
https://docs.pydantic.dev/1.10/usage/schema/
https://stackoverflow.com/questions/74607041/how-to-do-with-pydantic-regex-validation

TESTS:
https://www.youtube.com/watch?v=bMk5a10KeVc
https://stackoverflow.com/questions/53125305/testing-logging-output-with-pytest
https://github.com/fastapi/fastapi/issues/1273
<!-- asctime_pattern = '[0-9]{4}-[0-1][0-9]-[0-3][0-9] [0-2][0-9]:[0-6][0-9]:[0-6][0-9],[0-9]{3}' -->
start "C:\Program Files\Docker\Docker\Docker Desktop.exe"
set-alias docker-start "C:\Program Files\Docker\Docker\Docker Desktop.exe"
Then just type "docker-start" on your terminal.


[fom](https://fastapi.tiangolo.com/ru/advanced/async-tests/)
If your application relies on lifespan events, the AsyncClient won't trigger these events. To ensure they are triggered, use LifespanManager from florimondmanca/asgi-lifespan.
https://github.com/florimondmanca/asgi-lifespan#usage
https://docs.pytest.org/en/stable/deprecations.html#calling-fixtures-directly
https://stackoverflow.com/questions/65051581/how-to-trigger-lifespan-startup-and-shutdown-while-testing-fastapi-app

[Throttler (Ограничитель) – это класс, отвечающий за ограничение количества одновременных операций, выполняемых с некоторым ресурсом (например, пул соединения, сетевой буфер или ресурсоемкие операции процессора).](https://habr.com/ru/companies/wix/articles/301644/)

<!-- 
E       fixture 'app' not found
>       available fixtures: _session_event_loop, ac, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, event_loop, event_loop_policy, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tests/test_uuid.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory
>       use 'pytest --fixtures [testpath]' for help on them. -->

<!-- 
# SETUP (recomended way)
@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
 -->

pip install fastapi[all]
переделать requirements
pip freeze > requirements.txt
pip install -r requirements.txt
Python 3.12.3
RabbitMQ version: 3.13.4
docker-compose up
сделать новые requirements с pika


### RabbitMQ

Comand to enable RabbitMQ GUI by [link](http://127.0.0.1:15672/)

```shell
rabbitmq-plugins enable rabbitmq_management
```

* login: rmuser
* password: rmpassword

Other useful commands

```shell
rabbitmqctl help
rabbitmqctl status
rabbitmqctl shutdown
rabbitmqctl start_app
```

2. RabbitMQ 3.13.4
[direct link](https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.13.4/rabbitmq-server-3.13.4.exe)
3. Erlang 26.2.5.2
[direct link](https://github.com/erlang/otp/releases/download/OTP-26.2.5.2/otp_win64_26.2.5.2.exe)

<!-- не работало -->
CMD [ "uvicorn", "uvicorn code.src.main:app"]
uvicorn main:app --reload --reload-exclude "*.log"

pip install pytest pytest-asyncio
pytest tests/
pytest -v tests/

# RabbitMQ
Interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
Interface: [::], port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0
Interface: 0.0.0.0, port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0

Starting node rabbit@localhost 

rabbitmqctl help
rabbitmqctl status
rabbitmqctl shutdown
rabbitmqctl start_app
rabbitmq-plugins enable rabbitmq_management

rabbitmqctl add_user roger rabbit
rabbitmqctl set_user_tags roger administrator
rabbitmqctl set_permissions -p / roger ".*" ".*" ".*"

http://127.0.0.1:5672

C:\Program Files\RabbitMQ Server\rabbitmq_server-3.13.4\sbin

15672 - managment default port in RabbitMQ Assistant
docker pull rabbitmq

Docker запускает Engine 5min or more
docker scout quickview rabbitmq
What's next:
    View vulnerabilities → docker scout cves rabbitmq
    View base image update recommendations → docker scout recommendations rabbitmq
    Include policy results in your quickview by supplying an organization → docker scout quickview rabbitmq --org <organization>

$ docker run -d --hostname my-rabbit --name some-rabbit rabbitmq:3

docker run -d --name my-rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

19569f6427e4e22241bdef54a2eb4e7d9aad15b82e722e0ccf9e23c5d72bc908

docker start some-rabbit

docker ps -a

login:     guest
password:  guest

RabbitMQ 3.13.4 Erlang 26.2.5.2
В рабочем образе:
RabbitMQ 3.8.19-rc.1 Erlang 24.0.3

durable - в случае перезагрузки созданные обменники не удалятся
transient - удалятся

добавить обченник добавить очередь
привязать очереди к обменникам


python-pika
https://pypi.org/project/pika/

rabbitmq in docker
https://www.rabbitmq.com/docs/download

# Docker deployment
https://www.google.com/search?q=how+to+deploy+docker+compose&oq=how+todeploy+dock&gs_lcrp=EgZjaHJvbWUqCQgBEAAYDRiABDIGCAAQRRg5MgkIARAAGA0YgAQyCQgCEAAYDRiABDIJCAMQABgNGIAEMgkIBBAAGA0YgAQyCQgFEAAYDRiABDIJCAYQABgNGIAEMgkIBxAAGA0YgAQyCQgIEAAYDRiABDIJCAkQABgNGIAE0gEJMTE4MjNqMWo3qAIAsAIA&sourceid=chrome&ie=UTF-8
https://www.docker.com/blog/how-to-deploy-on-remote-docker-hosts-with-docker-compose/
https://www.reddit.com/r/devops/comments/soagh3/how_to_deploy_my_first_docker_compose_application/
https://dashboard.heroku.com/apps


https://stackoverflow.com/questions/65217124/docker-rabbitmq-and-pike-connection-refused
2024-07-28 10:38:39 2024-07-28 07:38:39.817 [info] <0.877.0> accepting AMQP connection <0.877.0> (172.18.0.4:35412 -> 172.18.0.2:5672)

# Packages that exist in test app, but doesn't exist in fastapi[all]
alembic==1.13.1
async-timeout==4.0.3
asyncpg==0.29.0
bcrypt==4.1.2
cffi==1.16.0
coverage==7.4.0
cryptography==41.0.7
Faker==22.0.0
greenlet==3.0.3
gunicorn==21.2.0
iniconfig==2.0.0
Mako==1.3.0
packaging==23.2
pluggy==1.3.0
pycparser==2.21
PyJWT==2.8.0
pytest==7.4.3
pytest-asyncio==0.23.3
pytest-cov==4.1.0
python-dateutil==2.8.2
six==1.16.0
SQLAlchemy==2.0.23
uvloop==0.19.0

# Activate/deactivate virtual env
```shell
./env/Scripts/Activate.ps1
deactivate
```

http://localhost:8000/api/docs


# for produser
# https://stackoverflow.com/questions/69210200/publish-a-message-to-the-right-queue-of-rabbitmq-from-python-pika-for-consumpt
# https://github.com/pika/pika/issues/1324

# https://www.rabbitmq.com/docs/cli
# https://www.rabbitmq.com/docs/install-windows#installer
# https://pypi.org/project/pika/
# amqp

# for confest
# @pytest.fixture(autouse=True, scope='session')
# def event_loop(prepare_database):
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield(loop)
#     loop.close()