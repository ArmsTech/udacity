"""Add some seed data.

Revision ID: cf1afd1ebfb
Revises: None
Create Date: 2015-11-28 21:19:04.587643

"""

# revision identifiers, used by Alembic.
revision = 'cf1afd1ebfb'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

from tech_quote.categories import ALL_CATEGORIES

category_table = table(
    'category',
    column('category_id', sa.Integer),
    column('category_name', sa.String),
    column('category_description', sa.String),
    column('category_icon_url', sa.String))


def upgrade():
    op.bulk_insert(category_table, ALL_CATEGORIES)


def downgrade():
    connection = op.get_bind()
    connection.execute(
        "DELETE FROM category WHERE category_name IN ('Python','JavaScript');")
