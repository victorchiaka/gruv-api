from fastapi import APIRouter

router = APIRouter(tags=["users"], responses={404: {"description": "Not found"}})


@router.post("/register")
async def register():
    pass


@router.get("/whoami")
async def whoami():
    pass
