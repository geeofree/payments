"""drop user_roles table

Revision ID: 263a99abbfcb
Revises: 58c1a6d8bb89
Create Date: 2023-05-11 18:40:52.994990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '263a99abbfcb'
down_revision = '58c1a6d8bb89'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("user_roles")


def downgrade() -> None:
    op.create_table(
        "user_roles",
        # Identifiers
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id', ondelete="CASCADE"), nullable=False),
        sa.Column('role_id', sa.Integer, sa.ForeignKey('roles.id', ondelete="CASCADE"), nullable=False),

        # Timestamps
        sa.Column('created_at', sa.DateTime, server_default=sa.sql.func.now()),
        sa.Column('updated_at', sa.DateTime, onupdate=sa.sql.func.now()),

        # Constraints
        sa.UniqueConstraint('user_id', 'role_id'),
    )
