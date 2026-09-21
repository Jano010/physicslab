import httpx
from httpx import Response


async def test_health(client: httpx.AsyncClient) -> None:
    r : Response = await client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok", "version": "0.1.0"}
