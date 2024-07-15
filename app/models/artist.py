import uuid
from datetime import datetime

from sqlalchemy import UUID, Column, DateTime, String, Text
from sqlalchemy.orm import relationship

from ..utils.database import Base


class Artist(Base):
    __tablename__ = "artists"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4())
    name = Column(String, nullable=False)
    bio = Column(Text)
    created_at = Column(DateTime, default=datetime.now())

    albums = relationship("Album", back_populates="artists")
    songs = relationship("Song", back_populates="artists")
