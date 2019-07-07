"""add created updated

Revision ID: 675855158a90
Revises: b3ad8c177ef3
Create Date: 2019-06-23 15:39:11.914235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '675855158a90'
down_revision = 'b3ad8c177ef3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventory', sa.Column('created', sa.DateTime(), nullable=True))
    op.add_column('inventory', sa.Column('updated', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inventory', 'updated')
    op.drop_column('inventory', 'created')
    # ### end Alembic commands ###
