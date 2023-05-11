"""create role_abilities table

Revision ID: 58c1a6d8bb89
Revises: 96794382b7cf
Create Date: 2023-05-11 17:52:41.898985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58c1a6d8bb89'
down_revision = '96794382b7cf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "abilities",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("uuid", sa.Uuid, nullable=False, unique=True),

        sa.Column("name", sa.String(64), nullable=False, unique=True),
        sa.Column("description", sa.String, nullable=True),

        sa.Column('created_at', sa.DateTime, server_default=sa.sql.func.now()),
        sa.Column('updated_at', sa.DateTime, onupdate=sa.sql.func.now()),
    )
    op.create_table(
        "role_abilities",
        sa.Column("role_id", sa.Integer, sa.ForeignKey("roles.id", ondelete="CASCADE"), nullable=False),
        sa.Column("ability_id", sa.Integer, sa.ForeignKey("abilities.id", ondelete="CASCADE"), nullable=False),

        # Timestamps
        sa.Column('created_at', sa.DateTime, server_default=sa.sql.func.now()),
        sa.Column('updated_at', sa.DateTime, onupdate=sa.sql.func.now()),
    )


def downgrade() -> None:
    op.drop_table("role_abilities")
    op.drop_table("abilities")
