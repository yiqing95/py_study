__author__ = 'yiqing'

from sqlalchemy import create_engine, MetaData ,Table
from sqlalchemy.orm import sessionmaker

from sqlalchemy.sql import select

import pymysql

#  DB_CONN_STR = 'mysql+mysqldb://root:@localhost/test?charset=utf8'
# 选择低层的msyql库为pymysql！
engine = create_engine('mysql+pymysql://root:@localhost/yiicoders?charset=utf8')

conn = engine.connect()
metadata = MetaData()

DB_SESSION = sessionmaker(bind=engine)

session = DB_SESSION()

# 创建db
# session.execute('create database my_python')
print(session.execute('show databases').fetchall())




def table_test():
    tbl_msg = Table('msg',metadata,autoload=True,autoload_with=engine)
    select_obj = select([tbl_msg])
    try:
        rs = conn.execute(select_obj)
        for row in rs:
            print(row)

    except Exception as ex:
        raise
    finally:
        conn.close()
