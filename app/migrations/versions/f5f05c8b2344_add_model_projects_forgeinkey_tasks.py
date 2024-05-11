"""add model projects forgeinkey tasks

Revision ID: f5f05c8b2344
Revises: 7eb510894493
Create Date: 2024-05-11 17:32:05.705726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5f05c8b2344'
down_revision: Union[str, None] = '7eb510894493'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('date_create', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.add_column('tasks', sa.Column('prod_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tasks', 'projects', ['prod_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'prod_id')
    op.drop_table('projects')
    # ### end Alembic commands ###
