"""empty message

Revision ID: 150784ec1f93
Revises: 
Create Date: 2022-12-27 21:35:22.711608

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '150784ec1f93'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.String(length=20),
               nullable=False,
               existing_server_default=sa.text("''"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=20),
               type_=mysql.VARCHAR(length=255),
               nullable=True,
               existing_server_default=sa.text("''"))

    # ### end Alembic commands ###
