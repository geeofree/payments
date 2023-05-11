import sqlalchemy as sa
from .base import Base

role_ability = sa.Table(
    "role_abilities",
    Base.metadata,
    sa.Column("role_id", sa.Integer, sa.ForeignKey("roles.id", ondelete="CASCADE"), nullable=False),
    sa.Column("ability_id", sa.Integer, sa.ForeignKey("abilities.id", ondelete="CASCADE"), nullable=False),

    # Timestamps
    sa.Column('created_at', sa.DateTime, server_default=sa.sql.func.now()),
    sa.Column('updated_at', sa.DateTime, onupdate=sa.sql.func.now()),
)
