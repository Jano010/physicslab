from collections.abc import AsyncGenerator

import httpx
import pytest

from physicslab.main import app


@pytest.fixture
async def client() -> AsyncGenerator[httpx.AsyncClient]:
    async with httpx.AsyncClient(
    transport=httpx.ASGITransport(app=app),
    base_url="http://test"
    ) as c:
        yield c
