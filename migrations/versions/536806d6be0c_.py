"""empty message

Revision ID: 536806d6be0c
Revises: ca641829a5e0
Create Date: 2021-07-16 21:11:28.929007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '536806d6be0c'
down_revision = 'ca641829a5e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cached_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('discriminator', sa.String(length=4), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('users', 'guild',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'guild',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_table('cached_users')
    # ### end Alembic commands ###