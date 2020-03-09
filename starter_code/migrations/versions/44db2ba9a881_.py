"""empty message

Revision ID: 44db2ba9a881
Revises: b298f1d07f68
Create Date: 2020-03-09 14:40:28.741398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44db2ba9a881'
down_revision = 'b298f1d07f68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('show', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    # ### end Alembic commands ###
