"""empty message

Revision ID: 7948666e4ff5
Revises: 1e3c044d8cec
Create Date: 2021-10-12 23:27:00.156785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7948666e4ff5'
down_revision = '1e3c044d8cec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.String(length=50), nullable=False),
    sa.Column('product_price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sec_users',
    sa.Column('id', sa.String(length=250), nullable=False),
    sa.Column('full_name', sa.String(length=250), nullable=True),
    sa.Column('username', sa.String(length=250), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('verification', sa.Integer(), nullable=False),
    sa.Column('rememberToken', sa.String(length=250), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=250), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=250), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rememberToken')
    )
    op.create_index(op.f('ix_sec_users_email'), 'sec_users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sec_users_email'), table_name='sec_users')
    op.drop_table('sec_users')
    op.drop_table('products')
    # ### end Alembic commands ###
