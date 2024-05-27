from typing import List
from uuid import UUID
from pydantic import BaseModel

from api.src.schema.playlist import Playlist


class SongBase(BaseModel):
    title: str
    duration: int


class SongCreate(SongBase):
    playlists: List[Playlist]

class Song(SongBase):
    id: UUID
    playlist_id: UUID

    class Config:
        orm_mode = True
