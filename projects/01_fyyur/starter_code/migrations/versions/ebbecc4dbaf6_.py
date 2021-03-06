"""empty message

Revision ID: ebbecc4dbaf6
Revises: 012f8ef91292
Create Date: 2022-03-08 00:02:27.816906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebbecc4dbaf6'
down_revision = '012f8ef91292'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.drop_column('venue', 'looking_for_talent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('looking_for_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('venue', 'seeking_venue')
    # ### end Alembic commands ###
