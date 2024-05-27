from fastapi import APIRouter


playlists = APIRouter()


@playlists.get("/")
async def all():
    """
    At this endpoint all playlists will be fetched and returned with every data, irrespective of the playlist
    """
    return {"message": "All playlists here"}
