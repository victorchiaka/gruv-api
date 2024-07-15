import uuid
from datetime import datetime

from sqlalchemy import UUID, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..utils.database import Base
from .shared import playlist_songs, user_songs


class Song(Base):
    __tablename__ = "songs"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4())
    title = Column(String, nullable=False, index=True)
    duration = Column(Integer, nullable=False)
    album_id = Column(UUID(as_uuid=True), ForeignKey("albums.id"))
    artist_id = Column(UUID(as_uuid=True), ForeignKey("artists.id"))
    uploaded_at = Column(DateTime, default=datetime.now())

    album = relationship("Album", back_populates="songs")
    artist = relationship("Artist", back_populates="songs")
    playlists = relationship(
        "Playlist", secondary=playlist_songs, back_populates="songs"
    )
    liked_by_users = relationship(
        "User", secondary=user_songs, back_populates="liked_songs"
    )
