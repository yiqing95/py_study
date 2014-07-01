__author__ = 'yiqing'

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column,Integer,String
from sqlalchemy import create_engine
engine = create_engine('sqlite:///test3.db',echo=True)

Base = declarative_base()

print(Base)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    fullname = Column(String)
    # optional
    def __repr__(self):
        return '<User(%r,%r)>'%(
            self.name,self.fullname
        )

print(User.__table__)

obj_user = User(name='qing',fullname='yiqing')
print(obj_user)

print(obj_user.id)

# 接下来创建表了
Base.metadata.create_all(engine)

# 导入session
from sqlalchemy.orm import Session
session = Session(bind=engine)

session.add(obj_user)
print(session.new)

# 在内存中查询（对象使用IdentityMap管理的-- 主键是key）
# 查询后竟然自动持久化了！
our_user = session.query(User).filter_by(name='qing').first()
print(our_user)
print(our_user.id)

# 是不是同一个对象？ session 相同啦 对象一样
'''
print(obj_user is our_user)
id(our_user) == id(obj_user)
obj_user.someAttr = 'aho'
print(our_user.someAttr)
'''

# 以上全部还没有持久化到db 纯内存活动
# 下面存储到db
'''
session.add(
    [
        User(name='andy',fullname='Andy xx'),
        User(name='mary',fullname='Mary xx'),
        User(name='fred',fullname='Fred xx')
    ]
)
'''
print(session.new)
print(session.dirty)

session.commit()

class Network(Base):
    __tablename__ = 'network'
    network_id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)

Base.metadata.create_all(engine)

session.add_all([
    Network(name='netl'),
    Network(name='net2'),
])
session.flush()

query = session.query(User).filter(User.name== 'qing').\
order_by(User.id)
print(query.all())

for row in session.query(User,User.name):
    print(row.User,row.name)

from sqlalchemy import or_
for name , in session.query(User.name).filter(or_(User.fullname == 'hiih',User.id == 5)):
    print(name)

query = session.query(User).filter_by(fullname='yiqing')
print(query)
query.all()
query.first()
# query.one()
q = session.query(User.fullname)
q.all()
q2 = q.filter(or_(User.name=='nary',User.name=='ed'))
# q2[1]

from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationships

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer,primary_key=True)
    email_address = Column(String,nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))

    # user = relationships('User',backref = 'addresses')

    def __repr__(self):
        # return '<Address(%s)>' % self.email_address
        return '<Address(%r)>' % self.email_address

Base.metadata.create_all(engine)

session.query(User,Address).filter(User.id == Address.user_id).all()