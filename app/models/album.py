import uuid

from sqlalchemy import UUID, Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from ..utils.database import Base


class Album(Base):
    __tablename__ = "albums"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4())
    title = Column(String, nullable=False)
    release_date = Column(DateTime)
    artist_id = Column(UUID(as_uuid=True), ForeignKey("artists.id"))

    artist = relationship("Artist", back_populates="albums")
    songs = relationship("Song", back_populates="album")
