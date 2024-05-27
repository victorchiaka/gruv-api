from fastapi import FastAPI
from .src.routes.auth import auth
from .src.routes.songs import songs
from .src.routes.playlists import playlists
from .src.db.database import engine
from .src.models import user, song, playlist

"""
This file initializes the whole app
"""

user.Base.metadata.create_all(bind=engine)
song.Base.metadata.create_all(bind=engine)
playlist.Base.metadata.create_all(bind=engine)

app: FastAPI = FastAPI(
    title="Gruv API",
    description="API for Gruv music music streaming app",
    version="0.0.1",
)


base_url: str = "/api"

app.include_router(auth, prefix=f"{base_url}/auth")
app.include_router(playlists, prefix=f"{base_url}/playlist")
app.include_router(songs, prefix=f"{base_url}/song")
