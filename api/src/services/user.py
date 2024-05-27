from uuid import UUID
from sqlalchemy.orm import Session

from api.src.schema.user import UserCreate


def create_user(db: Session, user: UserCreate):
    # Do the necessary and create user
    pass


def get_user(db: Session, user_id: UUID):
    # Do the necessary and get user
    pass
