# app/alembic/versions/xxxx_add_deleted_at_to_todos.py
"""add deleted_at to todos

Revision ID: a1b2c3d4e5f6
Revises: 5e6c7566190d
Create Date: 2026-03-20 10:00:00.000000
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, Sequence[str], None] = '5e6c7566190d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'todos',
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True)
    )


def downgrade() -> None:
    op.drop_column('todos', 'deleted_at')