import pytest
from httpx import AsyncClient, ASGITransport
import asyncio
from async_asgi_testclient import TestClient
from asgi_lifespan import LifespanManager
import pytest_asyncio
from contextlib import asynccontextmanager

from src.main import app
# from src.main import App

# @pytest_asyncio.fixture
# async def app():
#     @asynccontextmanager
#     async def lifespan(app: App):
#         print("Starting up")
#         yield
#         print("Shutting down")

#     app = App(
#         title="Get UUID",
#         docs_url="/api/docs",
#         openapi_url="/api/openapi.json",
#         lifespan=lifespan,
#     )

#     async with LifespanManager(app) as manager:
#         print("We're in!")
#         yield manager.app

@pytest_asyncio.fixture(scope='session')
async def ac():
    # async with LifespanManager(app):
        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
            yield ac

# @pytest.fixture(scope='session')
# async def ac():
#     async with TestClient(app) as ac:
#         yield ac


# @pytest.fixture(scope='session')
# async def ac():
#     async with AsyncClient(app=app, base_url='http://test') as ac:
#         yield ac
