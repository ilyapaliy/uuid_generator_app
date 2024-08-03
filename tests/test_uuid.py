import pytest
from fastapi.testclient import TestClient
from src.main import app
import re
import time
# import os
# from unittest.mock import patch
# from httpx import AsyncClient
# import sys

uuid_pattern = '[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}'
# uuid_pattern = '[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[a-f0-9]{4}-?[a-f0-9]{12}'
re_uuid = re.compile('^' + uuid_pattern + '$', re.I)


# @pytest.mark.anyio
# async def test_root():
#     async with AsyncClient(app=app, headers={"X-Flag": "green"}, base_url="http://localhost:8000") as ac:
#         response = await ac.get("/generate-uuid")
#     assert response.status_code == 200
#     uuid = response.json()["uuid"]
#     assert re_uuid.match(uuid)

def test_x_flag_green():
    with TestClient(app, headers={"X-Flag": "green"}) as client:
        response = client.get("generate-uuid")
        assert response.status_code == 200
        uuid = response.json()["uuid"]
        assert re_uuid.match(uuid)


def test_x_flag_red():
    with TestClient(app, headers={"X-Flag": "red"}) as client:
        response = client.get("generate-uuid")
        assert response.status_code == 200
        uuid = response.json()["uuid"]
        assert re_uuid.match(uuid)


def test_is_uuid_random():
    with TestClient(app, headers={"X-Flag": "red"}) as client:
        response = client.get("generate-uuid")
        uuid1 = response.json()["uuid"]
        response = client.get("generate-uuid")
        uuid2 = response.json()["uuid"]
        assert uuid1 != uuid2


# @pytest.mark.asyncio()
# @patch("logging.root._log")

def test_is_green_flag_logged(caplog):
    with TestClient(app, headers={"X-Flag": "green"}) as client:
        client.get("generate-uuid")
        re_log = re.compile('[^"]*UUID: ' + uuid_pattern + ' - X-Flag: XFlag.green[^"]*', re.I)
        x_flag_green_log = re_log.search(caplog.text)
        assert x_flag_green_log != None


def test_is_red_flag_logged(caplog):
    with TestClient(app, headers={"X-Flag": "red"}) as client:
        client.get("generate-uuid")
        re_log = re.compile('[^"]*UUID: ' + uuid_pattern + ' - X-Flag: XFlag.red[^"]*', re.I)
        time.sleep(0.3)  # work with the RabbitMQ is not instantaneous, may be failed test if no waited time
        x_flag_red_log = re_log.search(caplog.text)
        assert x_flag_red_log != None

