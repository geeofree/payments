from uuid import uuid4
import sqlalchemy as sa
from database import db

User = sa.Table(
    'users',
    db.metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("uuid", sa.Uuid, nullable=False, unique=True, default=uuid4),

    sa.Column("username", sa.String(64), nullable=False, unique=True),
    sa.Column("password", sa.String, nullable=False),
    sa.Column("email", sa.String),

    sa.Column("first_name", sa.String(64)),
    sa.Column("last_name", sa.String(64)),
    sa.Column("date_of_birth", sa.Date),

    sa.Column("created_at", sa.DateTime, server_default=sa.sql.func.now()),
    sa.Column("updated_at", sa.DateTime, onupdate=sa.sql.func.now()),
)
