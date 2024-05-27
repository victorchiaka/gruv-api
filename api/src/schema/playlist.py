from pydantic import BaseModel
from uuid import UUID
from typing import List
from api.src.schema.song import Song
from api.src.models.user import User


class PlaylistBase(BaseModel):
    title: str
    songs: List[Song]


class PlaylistCreate(BaseModel):
    owner: User


class Playlist(BaseModel):
    id: UUID
    owner_id: UUID
