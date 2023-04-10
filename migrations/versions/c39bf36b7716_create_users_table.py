"""create users table

Revision ID: c39bf36b7716
Revises: 
Create Date: 2023-04-10 10:57:44.481438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c39bf36b7716'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        # Identifiers
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uuid', sa.Uuid, nullable=False, unique=True),

        # Account details
        sa.Column('username', sa.String(64), nullable=False, unique=True),
        sa.Column('password', sa.String, nullable=False, unique=True),
        sa.Column('email', sa.String, unique=True),

        # Personal details
        sa.Column('first_name', sa.String(64)),
        sa.Column('last_name', sa.String(64)),
        sa.Column('date_of_birth', sa.Date),

        # Timestamps
        sa.Column('created_at', sa.DateTime, server_default=sa.sql.func.now()),
        sa.Column('updated_at', sa.DateTime, onupdate=sa.sql.func.now()),
    )


def downgrade() -> None:
    op.drop_table('users')
