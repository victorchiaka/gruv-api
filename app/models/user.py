import uuid
from datetime import datetime

from sqlalchemy import UUID, Column, DateTime, Enum, String
from sqlalchemy.orm import relationship

from ..utils.constants import Role
from ..utils.database import Base
from .shared import user_songs


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4())
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)
    role = Column(Enum(Role), nullable=False, default=Role.USER)  # USER, ADMIN

    playlists = relationship("Playlist", back_populates="user")
    liked_songs = relationship(
        "Song", secondary=user_songs, back_populates="liked_by_users"
    )
