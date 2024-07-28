import pytest
from httpx import AsyncClient

from src.core.main import app


@pytest.fixture(scope='session')
async def ac():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac
