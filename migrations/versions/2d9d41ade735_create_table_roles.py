"""create table roles

Revision ID: 2d9d41ade735
Revises: 5c6da8f5086e
Create Date: 2018-12-31 13:59:40.929581

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2d9d41ade735'
down_revision = '5c6da8f5086e'
branch_labels = None
depends_on = None


def upgrade():
    roles_table = op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )

    op.bulk_insert(
        roles_table,
        [
            {"name": "user", "id": 1},
            {"name": "admin", "id": 2},
            {"name": "guest", "id": 3},
        ]
    )


def downgrade():
    op.drop_table('roles')
