"""forgeinkey project with users4

Revision ID: 6e3f1b7a3282
Revises: c6e829af35a2
Create Date: 2024-05-11 18:29:01.669454

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e3f1b7a3282'
down_revision: Union[str, None] = 'c6e829af35a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('prod_id', sa.Integer(), nullable=True))
    op.drop_constraint('users_project_id_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'projects', ['prod_id'], ['id'])
    op.drop_column('users', 'project_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_project_id_fkey', 'users', 'projects', ['project_id'], ['id'])
    op.drop_column('users', 'prod_id')
    # ### end Alembic commands ###