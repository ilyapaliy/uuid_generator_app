from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from src.main import app
import re
import time


uuid_pattern = '[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}'
re_uuid = re.compile('^' + uuid_pattern + '$', re.I)


async def test_green_flag(ac: AsyncClient, caplog):
    ac.headers = {"X-Flag": "green"}

    response = await ac.get("generate-uuid/")
    assert response.status_code == 200

    uuid = response.json()["uuid"]
    assert re_uuid.match(uuid)

    re_log = re.compile('[^"]*UUID: ' + uuid_pattern + ' - X-Flag: XFlag.green[^"]*', re.I)
    x_flag_green_log = re_log.search(caplog.text)
    assert x_flag_green_log != None


async def test_red_flag(ac: AsyncClient, caplog):
    ac.headers = {"X-Flag": "red"}

    async with LifespanManager(app):
        response = await ac.get("generate-uuid/")

    assert response.status_code == 200
    uuid = response.json()["uuid"]
    assert re_uuid.match(uuid)

    re_log = re.compile('[^"]*UUID: ' + uuid_pattern + ' - X-Flag: XFlag.red[^"]*', re.I)
    time.sleep(0.2)  # work with the RabbitMQ is not instantaneous, may be failed test if no waited time
    x_flag_red_log = re_log.search(caplog.text)
    assert x_flag_red_log != None


async def test_uuid_randomness(ac: AsyncClient):
    ac.headers = {"X-Flag": "green"}
    response = await ac.get("generate-uuid/")
    uuid1 = response.json()["uuid"]
    response = await ac.get("generate-uuid/")
    uuid2 = response.json()["uuid"]
    assert uuid1 != uuid2


async def test_uuid_bad_flag(ac: AsyncClient):
    ac.headers = {"X-Flag": "bad_random_text"}
    response = await ac.get("generate-uuid/")
    awaited_json_respose = {'detail': [{'type': 'enum', 'loc': ['header', 'X-Flag'], 'msg': "Input should be 'green' or 'red'", 'input': 'bad_random_text', 'ctx': {'expected': "'green' or 'red'"}}]}
    assert response.json() == awaited_json_respose


async def test_uuid_no_flag(ac: AsyncClient):
    ac.headers = {}
    response = await ac.get("generate-uuid/")
    uuid = response.json()["uuid"]
    assert re_uuid.match(uuid)