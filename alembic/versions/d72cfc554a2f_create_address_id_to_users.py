"""Create address_id to users

Revision ID: d72cfc554a2f
Revises: e9b935ee1c9f
Create Date: 2023-05-04 09:22:45.541079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd72cfc554a2f'
down_revision = 'e9b935ee1c9f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('address_id', sa.Integer(),nullable=True))
    op.create_foreign_key('address_users_fk',source_table='users',referent_table='address',
                          local_cols=["address_id"],remote_cols=['id'],ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('address_users_fk',table_name="users")
    op.drop_column('users','address_id')
