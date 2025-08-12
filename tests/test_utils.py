import pytest
from httpx import *

from main import app


@pytest.mark.asyncio
async def test_get_testfile():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        response = await ac.get("/testfile")
        assert response.status_code == 200

        data = response.json()
        assert len(data) == 1


@pytest.mark.asyncio
async def test_add_testfile():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        response = await ac.post("/testfile", json={"name": "Ilya", "age": 19})
        assert response.status_code == 200
        assert response.json() == {"success": True}
