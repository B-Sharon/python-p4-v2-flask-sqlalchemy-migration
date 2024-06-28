"""rename department

Revision ID: 6aedb34cad09
Revises: ea98c2583af5
Create Date: 2024-06-28 11:30:27.221775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aedb34cad09'
down_revision = 'ea98c2583af5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###