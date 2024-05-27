from typing import List
from uuid import UUID
from pydantic import BaseModel

from api.src.schema.playlist import Playlist


class UserCreate(BaseModel):
    username: str
    email: str
    hashed_password: str


class UserLogin(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: UUID
    username: str
    email: str
    password: str
    playlists: List[Playlist]

    class Config:
        orm_mode = True
