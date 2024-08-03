from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from src.main import app
import time
from schemas import UUIDResponse, XFlag, UUID


async def test_green_flag(ac: AsyncClient, caplog):
    ac.headers = {"X-Flag": "green"}

    response = await ac.get("generate-uuid/")
    assert response.status_code == 200

    assert isinstance(UUIDResponse.model_validate_json(response.text), UUIDResponse)

    words = caplog.text.split()
    words_to_validate = []
    for word in words:
        if word == str(XFlag.green):
            index = words.index(word)
            for i in range(5):
                words_to_validate.append(words[index - 4 + i])

    assert words_to_validate[0] == "UUID:"
    assert UUID(words_to_validate[1])
    assert words_to_validate[2] == "-"
    assert words_to_validate[3] == "X-Flag:"
    assert words_to_validate[4] == str(XFlag.green)


async def test_red_flag(ac: AsyncClient, caplog):
    ac.headers = {"X-Flag": "red"}

    async with LifespanManager(app):
        response = await ac.get("generate-uuid/")

    assert response.status_code == 200
    assert isinstance(UUIDResponse.model_validate_json(response.text), UUIDResponse)

    time.sleep(0.2)  # work with the RabbitMQ is not instantaneous, may be failed test if no waited time

    words = caplog.text.split()
    words_to_validate = []
    for word in words:
        if word == str(XFlag.red):
            index = words.index(word)
            for i in range(5):
                words_to_validate.append(words[index - 4 + i])

    assert words_to_validate[0] == "UUID:"
    assert UUID(words_to_validate[1])
    assert words_to_validate[2] == "-"
    assert words_to_validate[3] == "X-Flag:"
    assert words_to_validate[4] == str(XFlag.red)


async def test_uuid_randomness(ac: AsyncClient):
    ac.headers = {"X-Flag": "green"}
    response = await ac.get("generate-uuid/")
    uuid1 = UUIDResponse.model_validate_json(response.text).uuid
    response = await ac.get("generate-uuid/")
    uuid2 = UUIDResponse.model_validate_json(response.text).uuid
    assert uuid1 != uuid2


async def test_uuid_bad_flag(ac: AsyncClient):
    ac.headers = {"X-Flag": "bad_random_text"}
    response = await ac.get("generate-uuid/")
    awaited_json_respose = {'detail': [{'type': 'enum', 'loc': ['header', 'X-Flag'], 'msg': "Input should be 'green' or 'red'", 'input': 'bad_random_text', 'ctx': {'expected': "'green' or 'red'"}}]}
    assert response.json() == awaited_json_respose


async def test_uuid_no_flag(ac: AsyncClient):
    ac.headers = {}
    response = await ac.get("generate-uuid/")
    assert response.status_code == 200
    assert isinstance(UUIDResponse.model_validate_json(response.text), UUIDResponse)
