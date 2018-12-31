"""crate contact details table

Revision ID: 0914772411f0
Revises: b0f4db6b4ef3
Create Date: 2018-12-31 13:32:44.199414

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0914772411f0'
down_revision = 'b0f4db6b4ef3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'contact_details',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('phone_number', sa.String(50), nullable=False),
        sa.Column('address', sa.String(50)),
        sa.Column('actor_id', sa.Integer, sa.ForeignKey('actors.id'), nullable=False),
    )


def downgrade():
    op.drop_table('contact_details')
