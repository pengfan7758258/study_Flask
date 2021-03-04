"""empty message

Revision ID: 05919b5ad70d
Revises: 
Create Date: 2021-03-04 16:22:01.196464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05919b5ad70d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('n_title', sa.String(length=16), nullable=True),
    sa.Column('n_content', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news')
    # ### end Alembic commands ###