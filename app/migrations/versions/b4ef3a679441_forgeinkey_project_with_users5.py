"""forgeinkey project with users5

Revision ID: b4ef3a679441
Revises: 6e3f1b7a3282
Create Date: 2024-05-11 18:32:01.356651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4ef3a679441'
down_revision: Union[str, None] = '6e3f1b7a3282'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_prod_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'prod_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('prod_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_prod_id_fkey', 'users', 'projects', ['prod_id'], ['id'])
    # ### end Alembic commands ###