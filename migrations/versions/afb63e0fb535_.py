"""empty message

Revision ID: afb63e0fb535
Revises: 
Create Date: 2022-07-12 18:47:49.223167

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'afb63e0fb535'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_index('R_14', table_name='user_project')
    op.drop_table('user_project')
    op.drop_table('company')
    op.drop_index('R_12', table_name='user_company')
    op.drop_table('user_company')
    op.drop_table('payment')
    op.drop_table('project')
    op.drop_index('email', table_name='users')
    op.drop_index('username', table_name='users')
    op.drop_table('users')
    op.drop_table('plane')
    op.drop_table('license')
    op.drop_index('R_1', table_name='auth')
    op.drop_index('R_10', table_name='auth')
    op.drop_table('auth')
    op.drop_table('modeling')
    op.drop_table('user')
    op.drop_table('crack_manage')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crack_manage',
    sa.Column('pID', mysql.CHAR(length=18), nullable=False),
    sa.Column('cID', mysql.CHAR(length=18), nullable=False),
    sa.Column('cName', mysql.CHAR(length=18), nullable=True),
    sa.Column('location', mysql.CHAR(length=18), nullable=True),
    sa.Column('size', mysql.CHAR(length=18), nullable=True),
    sa.ForeignKeyConstraint(['pID'], ['project.pID'], name='crack_manage_ibfk_1'),
    sa.PrimaryKeyConstraint('pID', 'cID'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('user',
    sa.Column('userID', mysql.CHAR(length=18), nullable=False),
    sa.Column('userName', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('userPassword', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('phone', mysql.CHAR(length=20), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('userID'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('modeling',
    sa.Column('pID', mysql.CHAR(length=18), nullable=False),
    sa.Column('mdID', mysql.CHAR(length=18), nullable=False),
    sa.Column('mNAME', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('path', mysql.VARCHAR(length=100), nullable=True),
    sa.ForeignKeyConstraint(['pID'], ['project.pID'], name='modeling_ibfk_1'),
    sa.PrimaryKeyConstraint('pID', 'mdID'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('auth',
    sa.Column('userID', mysql.CHAR(length=18), nullable=False),
    sa.Column('LID', mysql.CHAR(length=18), nullable=False),
    sa.Column('count', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('PayID', mysql.CHAR(length=18), nullable=False),
    sa.ForeignKeyConstraint(['LID'], ['license.LID'], name='auth_ibfk_2'),
    sa.ForeignKeyConstraint(['PayID'], ['payment.PayID'], name='auth_ibfk_3'),
    sa.ForeignKeyConstraint(['userID'], ['user.userID'], name='auth_ibfk_1'),
    sa.PrimaryKeyConstraint('userID', 'LID', 'PayID'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('R_10', 'auth', ['PayID'], unique=False)
    op.create_index('R_1', 'auth', ['LID'], unique=False)
    op.create_table('license',
    sa.Column('LID', mysql.CHAR(length=18), nullable=False),
    sa.Column('LicenseName', mysql.CHAR(length=18), nullable=True),
    sa.Column('grade', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('LID'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('plane',
    sa.Column('mID', mysql.CHAR(length=18), nullable=False),
    sa.Column('mName', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('altitude', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('latitude', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('longitude', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('indexs', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('PlanID', mysql.CHAR(length=18), nullable=False),
    sa.ForeignKeyConstraint(['mID'], ['project.pID'], name='plane_ibfk_1'),
    sa.PrimaryKeyConstraint('mID', 'PlanID'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('password', sa.BLOB(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('username', 'users', ['username'], unique=False)
    op.create_index('email', 'users', ['email'], unique=False)
    op.create_table('project',
    sa.Column('pID', mysql.CHAR(length=18), nullable=False),
    sa.Column('Pname', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('Pdate', mysql.DATETIME(), nullable=True),
    sa.Column('pManage', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('aID', mysql.CHAR(length=18), nullable=True),
    sa.PrimaryKeyConstraint('pID'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('payment',
    sa.Column('PayID', mysql.CHAR(length=18), nullable=False),
    sa.Column('pay', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('payInfo', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('payInfo2', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('payInfo3', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('PayID'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('user_company',
    sa.Column('departID', mysql.CHAR(length=18), nullable=False),
    sa.Column('userID', mysql.CHAR(length=18), nullable=False),
    sa.ForeignKeyConstraint(['departID'], ['company.departID'], name='user_company_ibfk_1'),
    sa.ForeignKeyConstraint(['userID'], ['user.userID'], name='user_company_ibfk_2'),
    sa.PrimaryKeyConstraint('departID', 'userID'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('R_12', 'user_company', ['userID'], unique=False)
    op.create_table('company',
    sa.Column('departID', mysql.CHAR(length=18), nullable=False),
    sa.Column('departName', mysql.CHAR(length=18), nullable=True),
    sa.Column('location', mysql.CHAR(length=18), nullable=True),
    sa.Column('phone', mysql.CHAR(length=18), nullable=True),
    sa.Column('email', mysql.CHAR(length=18), nullable=True),
    sa.PrimaryKeyConstraint('departID'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('user_project',
    sa.Column('userID', mysql.CHAR(length=18), nullable=False),
    sa.Column('pID', mysql.CHAR(length=18), nullable=False),
    sa.Column('Date', mysql.DATETIME(), nullable=True),
    sa.Column('writer', mysql.CHAR(length=18), nullable=True),
    sa.ForeignKeyConstraint(['pID'], ['project.pID'], name='user_project_ibfk_2'),
    sa.ForeignKeyConstraint(['userID'], ['user.userID'], name='user_project_ibfk_1'),
    sa.PrimaryKeyConstraint('userID', 'pID'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('R_14', 'user_project', ['pID'], unique=False)
    op.drop_table('Users')
    # ### end Alembic commands ###
