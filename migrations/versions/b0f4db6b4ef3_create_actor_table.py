"""create actor table

Revision ID: b0f4db6b4ef3
Revises: 
Create Date: 2018-12-31 13:16:28.949164

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b0f4db6b4ef3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'actors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('birthday', sa.DateTime),
    )


def downgrade():
    op.drop_table('actors')
