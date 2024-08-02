import pytest
from fastapi.testclient import TestClient
from src.main import app
import re
import os
# from httpx import AsyncClient


uuid_pattern = '[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}'
asctime_pattern = '[0-9]{4}-[0-1][0-9]-[0-3][0-9] [0-2][0-9]:[0-6][0-9]:[0-6][0-9],[0-9]{3}'
re_uuid = re.compile('^' + uuid_pattern + '$', re.I)



# @pytest.mark.anyio
# async def test_root():
#     async with AsyncClient(app=app, headers={"X-Flag": "green"}, base_url="http://localhost:8000") as ac:
#         response = await ac.get("/generate-uuid")
#     assert response.status_code == 200
#     uuid = response.json()["uuid"]
#     assert re_uuid.match(uuid)

async def test_x_flag_green():
    client = TestClient(app, headers={"X-Flag": "green"})
    response = client.get("generate-uuid")
    assert response.status_code == 200
    uuid = response.json()["uuid"]
    assert re_uuid.match(uuid)


def test_x_flag_red():
    client = TestClient(app, headers={"X-Flag": "red"})
    response = client.get("generate-uuid")
    assert response.status_code == 200
    uuid = response.json()["uuid"]
    assert re_uuid.match(uuid)


# def test_is_uuid_random():
#     client = TestClient(app, headers={"X-Flag": "red"})
#     response = client.get("generate-uuid")
#     uuid1 = response.json()["uuid"]
#     response = client.get("generate-uuid")
#     uuid2 = response.json()["uuid"]
#     assert uuid1 != uuid2


# def test_is_green_flag_logged():
#     with open(os.getcwd() + "/app.log") as file:
#         lines = [line.rstrip() for line in file]
#         re_log_line = re.compile('^' + asctime_pattern + ' - INFO - UUID: ' + uuid_pattern + ' - X-Flag: green$', re.I)
#         assert re_log_line.match(lines[-59])
#         x_flag = re_log_line.match(lines[-59]).group(0)[-5:]
#         assert x_flag == "green"
