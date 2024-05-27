from sqlalchemy import UUID, Column, ForeignKey, String, Uuid
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import _RelationshipDeclared

from .user import User
from ..db.database import Base


class Playlist(Base):
    __tablename__ = "playlists"

    id: Column[UUID] = Column(Uuid, unique=True, primary_key=True)
    title: Column[str] = Column(String(30), unique=True, index=True, nullable=False)
    owner_id: Column[UUID] = Column(Uuid, ForeignKey("users.id"))
    owner: _RelationshipDeclared["User"] = relationship(
        "User", back_populates="playlists"
    )
    song_id: Column[UUID] = Column(Uuid, ForeignKey("songs.id"))
    songs: _RelationshipDeclared["Song"] = relationship(
        "Song", back_populates="playlists"
    )
