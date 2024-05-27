from fastapi import APIRouter


auth = APIRouter()


@auth.post("/register")
async def register():
    return {"message": "register here"}


@auth.post("/login")
async def login():
    return {"message": "login here"}
