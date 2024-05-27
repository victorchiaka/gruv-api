from sqlalchemy import UUID, Column, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import _RelationshipDeclared

from ..db.database import Base


class Song(Base):
    __tablename__ = "songs"

    id: Column[UUID] = Column(Uuid, unique=True, primary_key=True)
    title: Column[str] = Column(String(11), index=True, nullable=False)
    duration: Column[int] = Column(Integer, default=0)
    playlist_id: Column[UUID] = Column(Uuid, ForeignKey("playlists.id"))
    playlists: _RelationshipDeclared["Playlist"] = relationship(
        "Playlist", back_populates="songs"
    )

    # Artist will be added later as app develops
