"""combine merchant and admin tables

Revision ID: 529925c0bf40
Revises: 570070a1b28b
Create Date: 2019-09-30 22:23:42.294743

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '529925c0bf40'
down_revision = '570070a1b28b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('inventory', 'admin_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.drop_index('fk_inventory_merchant_id_merchant', table_name='inventory')
    op.create_foreign_key(op.f('fk_inventory_admin_id_admin'), 'inventory', 'admin', ['admin_id'], ['id'])
    op.drop_column('inventory', 'merchant_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventory', sa.Column('merchant_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_constraint(op.f('fk_inventory_admin_id_admin'), 'inventory', type_='foreignkey')
    op.create_index('fk_inventory_merchant_id_merchant', 'inventory', ['merchant_id'], unique=False)
    op.alter_column('inventory', 'admin_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###