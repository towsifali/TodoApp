"""Create address table

Revision ID: e9b935ee1c9f
Revises: 3e4afe435780
Create Date: 2023-05-04 09:16:06.428707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9b935ee1c9f'
down_revision = '3e4afe435780'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id',sa.Integer(), nullable=False, primary_key="True"),
                    sa.Column('address1',sa.String(200),nullable="False"),
                    sa.Column('address2',sa.String(200),nullable="False"),
                    sa.Column('city',sa.String(50),nullable="False"),
                    sa.Column('state',sa.String(50),nullable="False"),
                    sa.Column('country',sa.String(50),nullable="False"),
                    sa.Column('postalcode',sa.String(5),nullable="False")
                    )


def downgrade() -> None:
    op.drop_table('address')
