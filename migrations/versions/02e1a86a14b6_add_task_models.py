"""add task models

Revision ID: 02e1a86a14b6
Revises: 9504084d44bb
Create Date: 2024-05-08 14:30:07.867291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02e1a86a14b6'
down_revision: Union[str, None] = '9504084d44bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('user_id', sa.Integer(), nullable=True),
            sa.Column('name_task', sa.String(length=100), nullable=False),
            sa.Column('description', sa.String(), nullable=True),
            sa.Column('date_create', sa.Date(), nullable=True),
            sa.Column('deadline', sa.Date(), nullable=False),
            sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
            sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    # ### end Alembic commands ###
