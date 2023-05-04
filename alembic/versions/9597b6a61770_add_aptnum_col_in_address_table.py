"""Add aptnum col in address table

Revision ID: 9597b6a61770
Revises: d72cfc554a2f
Create Date: 2023-05-04 09:46:45.096677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9597b6a61770'
down_revision = 'd72cfc554a2f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('address', sa.Column('aptnum', sa.String(5),nullable=True))


def downgrade() -> None:
    op.drop_column('address','aptnum')
