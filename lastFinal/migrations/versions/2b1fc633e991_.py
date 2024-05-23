"""empty message

Revision ID: 2b1fc633e991
Revises: be2fc3cdd81b
Create Date: 2024-05-23 17:23:02.429073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b1fc633e991'
down_revision = 'be2fc3cdd81b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.String(length=1000), nullable=True))
        batch_op.add_column(sa.Column('phone_number', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('phone_number')
        batch_op.drop_column('address')

    # ### end Alembic commands ###