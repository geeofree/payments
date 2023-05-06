from sqlalchemy.orm import mapped_column, relationship
import sqlalchemy as sa
from uuid import uuid4
from .base import Base
from .user_role import UserRole
from .role import Role

class User(Base):
    __tablename__ = 'users'

    id = mapped_column(sa.Integer, primary_key=True)
    uuid = mapped_column(sa.Uuid, nullable=False, unique=True, default=uuid4)

    username = mapped_column(sa.String(64), nullable=False, unique=True)
    password = mapped_column(sa.String, nullable=False)
    email = mapped_column(sa.String)

    first_name = mapped_column(sa.String(64))
    last_name = mapped_column(sa.String(64))
    date_of_birth = mapped_column(sa.Date)

    roles = relationship(Role, secondary=UserRole)

    created_at = mapped_column(sa.DateTime, server_default=sa.sql.func.now())
    updated_at = mapped_column(sa.DateTime, onupdate=sa.sql.func.now())

    def __repr__(self):
        return "<User(uuid={}, username={}, created_at={}, updated_at={})>".\
            format(self.uuid, self.username, self.created_at, self.updated_at)
