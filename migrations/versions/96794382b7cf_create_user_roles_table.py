"""create user_roles table

Revision ID: 96794382b7cf
Revises: 8e838de6e2a2
Create Date: 2023-05-05 12:13:33.666975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96794382b7cf'
down_revision = '8e838de6e2a2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user_roles",
        # Identifiers
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('role_id', sa.Integer, sa.ForeignKey('roles.id'), nullable=False),

        # Timestamps
        sa.Column('created_at', sa.DateTime, server_default=sa.sql.func.now()),
        sa.Column('updated_at', sa.DateTime, onupdate=sa.sql.func.now()),

        # Constraints
        sa.UniqueConstraint('user_id', 'role_id'),
    )


def downgrade() -> None:
    op.drop_table("user_roles")
