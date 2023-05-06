from sqlalchemy.orm import mapped_column, relationship
from uuid import uuid4
import sqlalchemy as sa
from .base import Base

class Role(Base):
    __tablename__ = 'roles'

    id = mapped_column(sa.Integer, primary_key=True)
    uuid = mapped_column(sa.Uuid, nullable=False, unique=True, default=uuid4)

    name = mapped_column(sa.String(64), nullable=False, unique=True)
    description = mapped_column(sa.String, nullable=True)

    created_at = mapped_column(sa.DateTime, server_default=sa.sql.func.now())
    updated_at = mapped_column(sa.DateTime, onupdate=sa.sql.func.now())

    def __repr__(self):
        return "<Role(uuid={}, name={}, created_at={}, updated_at={})>".\
            format(self.uuid, self.name, self.created_at, self.updated_at)
