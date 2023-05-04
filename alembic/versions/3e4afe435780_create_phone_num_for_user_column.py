"""create phone num for user column

Revision ID: 3e4afe435780
Revises: 
Create Date: 2023-04-13 15:41:38.191567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e4afe435780'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(11),nullable=True))


def downgrade():
    op.drop_column('users','phone_number')
