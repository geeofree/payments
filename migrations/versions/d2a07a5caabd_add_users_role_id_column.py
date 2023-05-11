"""add users.role_id column

Revision ID: d2a07a5caabd
Revises: 263a99abbfcb
Create Date: 2023-05-11 18:41:40.101840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2a07a5caabd'
down_revision = '263a99abbfcb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("users", recreate="always") as batch_op:
        batch_op.add_column(
            sa.Column("role_id", sa.Integer, sa.ForeignKey("roles.id", ondelete="SET NULL")),
            insert_after="uuid"
        )


def downgrade() -> None:
    op.drop_column("users", "role_id")
