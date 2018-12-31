"""crate stuntmen table

Revision ID: 5c6da8f5086e
Revises: 28c94eeb56d1
Create Date: 2018-12-31 13:54:49.110465

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5c6da8f5086e'
down_revision = '28c94eeb56d1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stuntmen',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('active', sa.Boolean, default=True),
        sa.Column('actor_id', sa.Integer, sa.ForeignKey('actors.id')),
    )


def downgrade():
    op.drop_table('stuntmen')
