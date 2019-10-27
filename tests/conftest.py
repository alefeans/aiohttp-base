import pytest
from aiohttp import web
from app.routes import setup_routes


@pytest.fixture
def cli(loop, aiohttp_client):
    app = web.Application()
    setup_routes(app)
    return loop.run_until_complete(aiohttp_client(app))
