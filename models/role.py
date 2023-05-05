from uuid import uuid4
import sqlalchemy as sa
from database import db

Role = sa.Table(
    'roles',
    db.metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("uuid", sa.Uuid, nullable=False, unique=True, default=uuid4),

    sa.Column("name", sa.String(64), nullable=False, unique=True),
    sa.Column("description", sa.String, nullable=True),

    sa.Column("created_at", sa.DateTime, server_default=sa.sql.func.now()),
    sa.Column("updated_at", sa.DateTime, onupdate=sa.sql.func.now()),
)
