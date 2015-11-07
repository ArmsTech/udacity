"""Add some seed data.

Revision ID: 29095d3cc367
Revises: None
Create Date: 2015-11-07 03:47:49.692382

"""

# revision identifiers, used by Alembic.
revision = '29095d3cc367'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

from tech_quote.categories import JAVASCRIPT, PYTHON

category_table = table(
    'category',
    column('category_id', sa.Integer),
    column('category_name', sa.String),
    column('category_description', sa.String),
    column('category_icon_url', sa.String))


def upgrade():
    op.bulk_insert(category_table, [PYTHON, JAVASCRIPT])


def downgrade():
    connection = op.get_bind()
    connection.execute(
        "DELETE FROM category WHERE category_name IN ('Python','JavaScript');")
