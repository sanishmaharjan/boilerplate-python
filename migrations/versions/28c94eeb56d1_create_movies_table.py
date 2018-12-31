"""crate movies table

Revision ID: 28c94eeb56d1
Revises: 0914772411f0
Create Date: 2018-12-31 13:47:27.735420

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '28c94eeb56d1'
down_revision = '0914772411f0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'movies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('release_date', sa.TIMESTAMP),
    )

    op.create_table(
        'movies_actors_association',
        sa.Column('movie_id', sa.Integer, sa.ForeignKey('movies.id', ondelete='CASCADE', onupdate='CASCADE'),
                  nullable=False),
        sa.Column('actor_id', sa.Integer, sa.ForeignKey('actors.id', ondelete='CASCADE', onupdate='CASCADE'),
                  nullable=False),
    )


def downgrade():
    op.drop_table('movies')
