from httpx import AsyncClient, ASGITransport
import pytest_asyncio
from src.main import app


@pytest_asyncio.fixture(scope='session')
async def ac():
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
        yield ac
