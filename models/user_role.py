import sqlalchemy as sa
from database import db

UserRole = sa.Table(
    "user_roles",
    db.metadata,
    sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
    sa.Column("role_id", sa.Integer, sa.ForeignKey("roles.id"), nullable=False),

    sa.Column("created_at", sa.DateTime, server_default=sa.sql.func.now()),
    sa.Column("updated_at", sa.DateTime, onupdate=sa.sql.func.now()),
)
