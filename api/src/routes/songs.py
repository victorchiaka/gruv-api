from fastapi import APIRouter


songs = APIRouter()


@songs.get("/")
async def all():
    """
    At this endpoint all songs will be fetched and returned with every data, irrespective of the playlist
    """
    return {"message": "get all songs"}
