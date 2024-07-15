from sqlalchemy import Column, DateTime, ForeignKey, Table, Uuid

from ..utils.database import Base

user_songs = Table(
    "user_songs",
    Base.metadata,
    Column("user_id", Uuid, ForeignKey("users.id"), primary_key=True),
    Column("song_id", Uuid, ForeignKey("songs.id"), primary_key=True),
    Column("liked_at", DateTime),
)

playlist_songs = Table(
    "playlist_id",
    Base.metadata,
    Column("playlist_id", Uuid, ForeignKey("playlists.id"), primary_key=True),
    Column("song_id", Uuid, ForeignKey("songs.id"), primary_key=True),
)
