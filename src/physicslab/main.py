from fastapi import FastAPI

from physicslab.experiments.router import register_experiments_exception_handlers
from physicslab.experiments.router import router as experiments_router

app = FastAPI()

app.include_router(experiments_router)
register_experiments_exception_handlers(app)



@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok", "version": "0.1.0"}
