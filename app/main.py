from fastapi import FastAPI

from .routers import users

app = FastAPI(
    title="Gruv API",
    description="API for Gruv music music streaming app",
    version="0.0.1",
)

app.include_router(users.router, prefix="/users")


@app.get("/")
async def health_check():
    return {"message": "Hello, World"}
