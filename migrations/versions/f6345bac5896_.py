"""empty message

Revision ID: f6345bac5896
Revises: d80cb96a2219
Create Date: 2025-03-26 11:49:53.084674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6345bac5896'
down_revision = 'd80cb96a2219'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        batch_op.create_unique_constraint('email', ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('email', type_='unique')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
