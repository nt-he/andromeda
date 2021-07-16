"""cleanliness updates

Revision ID: 5f2e3bfa372c
Revises: 59f58ec77d68
Create Date: 2021-07-06 18:38:32.458791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f2e3bfa372c'
down_revision = '59f58ec77d68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('discord_id', sa.INTEGER(), nullable=False),
    sa.Column('strikes', sa.INTEGER(), nullable=True),
    sa.Column('muted', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'discord_id')
    )
    # ### end Alembic commands ###