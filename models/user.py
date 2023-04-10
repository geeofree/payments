from sqlalchemy.orm import mapped_column
from uuid import uuid4
from . import BaseModel
import sqlalchemy as sa

class User(BaseModel):
    __tablename__ = 'users'

    id = mapped_column(sa.Integer, primary_key=True)
    uuid = mapped_column(sa.Uuid, nullable=False, unique=True, default=uuid4)

    username = mapped_column(sa.String(64), nullable=False, unique=True)
    password = mapped_column(sa.String, nullable=False, unique=True)
    email = mapped_column(sa.String, unique=True)

    first_name = mapped_column(sa.String(64))
    last_name = mapped_column(sa.String(64))
    date_of_birth = mapped_column(sa.Date)

    created_at = mapped_column(sa.DateTime, server_default=sa.sql.func.now())
    updated_at = mapped_column(sa.DateTime, onupdate=sa.sql.func.now())
