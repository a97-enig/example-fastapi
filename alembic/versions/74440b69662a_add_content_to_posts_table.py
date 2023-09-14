"""add content to posts table

Revision ID: 74440b69662a
Revises: c68d0f944999
Create Date: 2023-09-14 22:11:44.155192

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74440b69662a'
down_revision: Union[str, None] = 'c68d0f944999'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
