"""empty message

Revision ID: f8b293a1ade2
Revises: 58e25e9deb3c
Create Date: 2021-07-18 16:04:26.743245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8b293a1ade2'
down_revision = '58e25e9deb3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('guild', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'guild')
    # ### end Alembic commands ###
