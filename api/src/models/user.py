from sqlalchemy import UUID, Column, ForeignKey, String, Uuid
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import _RelationshipDeclared

from ..db.database import Base


class User(Base):
    __tablename__ = "users"

    id: Column[UUID] = Column(Uuid, unique=True, primary_key=True)
    email: Column[str] = Column(String, unique=True, index=True, nullable=False)
    username: Column[str] = Column(String, unique=True, index=True)
    hash_password: Column[str] = Column(String)
    playlist_id: Column[UUID] = Column(Uuid, ForeignKey("playlists.id"))
    playlists: _RelationshipDeclared["Playlist"] = relationship(
        "Playlist", back_populates="owner"
    )
