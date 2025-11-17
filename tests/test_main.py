import pytest
from httpx import AsyncClient, ASGITransport
import time

# Import your app from its location in the 'apps' folder
from apps.main import app


@pytest.mark.asyncio
async def test_root_endpoint():
    """
    Tests the main "/" endpoint.
    """
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, this is a secure FastAPI app!"}


@pytest.mark.asyncio
async def test_health_endpoint():
    """
    Tests the "/health" endpoint.
    """
    start_time = int(time.time())

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/health")

    end_time = int(time.time())

    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "healthy"
    assert isinstance(data["epoch_time"], int)
    assert start_time <= data["epoch_time"] <= end_time
