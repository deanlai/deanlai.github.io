"""changed grade to string

Revision ID: 2291eaf4bc3f
Revises: cef96f3db43c
Create Date: 2019-03-30 08:25:29.231998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2291eaf4bc3f'
down_revision = 'cef96f3db43c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('problem', sa.Column('complexity', sa.Integer(), nullable=True))
    op.add_column('problem', sa.Column('intensity', sa.Integer(), nullable=True))
    op.add_column('problem', sa.Column('risk', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_problem_complexity'), 'problem', ['complexity'], unique=False)
    op.create_index(op.f('ix_problem_intensity'), 'problem', ['intensity'], unique=False)
    op.create_index(op.f('ix_problem_risk'), 'problem', ['risk'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_problem_risk'), table_name='problem')
    op.drop_index(op.f('ix_problem_intensity'), table_name='problem')
    op.drop_index(op.f('ix_problem_complexity'), table_name='problem')
    op.drop_column('problem', 'risk')
    op.drop_column('problem', 'intensity')
    op.drop_column('problem', 'complexity')
    # ### end Alembic commands ###
