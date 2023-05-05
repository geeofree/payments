"""create roles table

Revision ID: 8e838de6e2a2
Revises: c39bf36b7716
Create Date: 2023-05-05 11:55:07.443876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e838de6e2a2'
down_revision = 'c39bf36b7716'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "roles",
        # Identifiers
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uuid', sa.Uuid, nullable=False, unique=True),

        # Role Details
        sa.Column("name", sa.String(64), nullable=False, unique=True),
        sa.Column("description", sa.String(64), nullable=True),

        # Timestamps
        sa.Column('created_at', sa.DateTime, server_default=sa.sql.func.now()),
        sa.Column('updated_at', sa.DateTime, onupdate=sa.sql.func.now()),
    )


def downgrade() -> None:
    op.drop_table("roles")
