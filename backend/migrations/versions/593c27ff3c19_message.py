"""message

Revision ID: 593c27ff3c19
Revises: 
Create Date: 2023-02-16 23:28:07.151778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '593c27ff3c19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.String(length=100), nullable=True),
    sa.Column('isfault', sa.Boolean(), nullable=True),
    sa.Column('faulttype', sa.String(length=100), nullable=True),
    sa.Column('faultplace', sa.String(length=100), nullable=True),
    sa.Column('faulttime', sa.DateTime(), nullable=True),
    sa.Column('issolved', sa.Boolean(), nullable=True),
    sa.Column('solvetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('warninginfo', sa.String(length=1000), nullable=True),
    sa.Column('areainfo', sa.String(length=1000), nullable=True),
    sa.Column('securityinfo', sa.String(length=1000), nullable=True),
    sa.Column('otherinfo', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=1000), nullable=True),
    sa.Column('author', sa.String(length=100), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('monitors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.String(length=100), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('usedyears', sa.Integer(), nullable=True),
    sa.Column('monitorplace', sa.String(length=100), nullable=True),
    sa.Column('fixedtime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('realname', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('department', sa.String(length=100), nullable=True),
    sa.Column('isused', sa.Boolean(), nullable=True),
    sa.Column('createtime', sa.DateTime(), nullable=True),
    sa.Column('isfaceused', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('license', sa.String(length=100), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('whyin', sa.String(length=100), nullable=True),
    sa.Column('isin', sa.Boolean(), nullable=True),
    sa.Column('intime', sa.DateTime(), nullable=True),
    sa.Column('outtime', sa.DateTime(), nullable=True),
    sa.Column('ownername', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=100), nullable=True),
    sa.Column('pay', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('visitors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('whyin', sa.String(length=100), nullable=True),
    sa.Column('isin', sa.Boolean(), nullable=True),
    sa.Column('intime', sa.DateTime(), nullable=True),
    sa.Column('outtime', sa.DateTime(), nullable=True),
    sa.Column('visitplace', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=100), nullable=True),
    sa.Column('company', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('warehouses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.String(length=100), nullable=True),
    sa.Column('capicity', sa.Integer(), nullable=True),
    sa.Column('used', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('warnings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('warningtype', sa.String(length=100), nullable=True),
    sa.Column('iswarn', sa.String(length=100), nullable=True),
    sa.Column('warnplace', sa.String(length=100), nullable=True),
    sa.Column('warntime', sa.DateTime(), nullable=True),
    sa.Column('issolved', sa.Boolean(), nullable=True),
    sa.Column('solvetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('warnings')
    op.drop_table('warehouses')
    op.drop_table('visitors')
    op.drop_table('vehicles')
    op.drop_table('users')
    op.drop_table('monitors')
    op.drop_table('log')
    op.drop_table('info')
    op.drop_table('facilities')
    # ### end Alembic commands ###
