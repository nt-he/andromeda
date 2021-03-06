"""empty message

Revision ID: 58e25e9deb3c
Revises: 59f58ec77d68
Create Date: 2021-07-17 09:48:37.273147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58e25e9deb3c'
down_revision = '59f58ec77d68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cached_users',
    sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('discriminator', sa.String(length=4), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cached_users')
    # ### end Alembic commands ###
