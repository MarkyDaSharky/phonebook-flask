"""empty message

Revision ID: 3fff7f4dcffb
Revises: d1a943c65247
Create Date: 2022-02-15 16:58:48.142936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fff7f4dcffb'
down_revision = 'd1a943c65247'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contact', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('email', sa.VARCHAR(length=150), nullable=False))
    # ### end Alembic commands ###
