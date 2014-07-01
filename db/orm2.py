__author__ = 'yiqing'


from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column,Integer,String
from sqlalchemy import create_engine

# 导入session
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///test3.db')
session = Session(bind=engine)


Base = declarative_base()


