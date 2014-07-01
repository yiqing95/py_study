__author__ = 'yiqing'

from sqlalchemy import MetaData
from sqlalchemy import Table,Column
from sqlalchemy import Integer,String

metadata = MetaData()
user_table = Table('user',metadata,
                   Column('id',Integer,primary_key=True),
                   Column('name',String),
                   Column('fullname',String)
                   )

print(user_table.name)

print(user_table.c.name)

print(user_table.columns.keys())

print(user_table.c,  user_table.primary_key)

print(user_table.select())


from sqlalchemy import create_engine
engine = create_engine('sqlite:///test2.db')
'''
metadata.create_all(engine)
'''

from sqlalchemy import String,Numeric,DateTime,Enum
fancy_table = Table('fancy',metadata,
                    Column('key',String(50),primary_key=True),
                    Column('timestamp',DateTime),
                    Column('amount',Numeric(10,2)),
                    Column('type',Enum('a','b','c'))
                    )

# fancy_table.create(engine)

from sqlalchemy import Unicode,UnicodeText,DateTime
from sqlalchemy import ForeignKeyConstraint,ForeignKey

story_table = Table('story',metadata,
                    Column('story_id',Integer,primary_key=True),
                    Column('version_id',Integer,primary_key=True),
                    Column('headline',Unicode(100),nullable=True),
                    Column('body',UnicodeText)
                    )
published_table = Table('published',metadata,
                        Column('pub_id',Integer,primary_key=True),
                        Column('pub_timestamp',DateTime,nullable=True),
                        Column('story_id',Integer),
                        Column('version_id',Integer),
                        ForeignKeyConstraint(
                            ['story_id','version_id'],
                            ['story.story_id','story.version_id']
                        )
)

# metadata.create_all(engine)

network_table =Table('network',metadata,
                     Column('network_id',Integer,primary_key=True),
                     Column('name',String(100),nullable=True),
                     Column('create_at',DateTime,nullable=True),
                     Column('owner_id',Integer,ForeignKey('user.id'))
                     )

print(network_table.c)
metadata.create_all(engine)

metadata2 = MetaData()
user_reflected = Table('user',metadata2,autoload=True,autoload_with=engine)
print(user_reflected)

from sqlalchemy import inspect
inspector = inspect(engine)
print(inspector)
print(inspector.get_columns('user'))

for tname in inspector.get_table_names():
    for col in inspector.get_columns(tname):
        if col['name'] == 'story_id':
            print(tname)

# ================================
from sqlalchemy import and_,or_
print(
    and_(
        user_table.c.fullname == 'ed jones',
        or_(
            user_table.c.name == 'ed',
            user_table.c.name == 'jack'
        )
    )
)

print(user_table.c.fullname == None)
print(user_table.c.fullname + 'some name')
print(user_table.c.fullname.in_(['1','3','3']))

expression = user_table.c.fullname == 'hi here'

from sqlalchemy.dialects import mysql
print(expression.compile(dialect=mysql.dialect()))

from sqlalchemy.dialects import postgresql
print(expression.compile(dialect=postgresql.dialect()))

import operator
print(operator.lt)

results = engine.execute(user_table.select().where(
    user_table.c.name == 'yi'
))
print(results.fetchall())

engine.execute(user_table.insert(),[
    {'name':'qing','fullname':'hiii'},
    {'name':'qing','fullname':'hii2'},
])

conn = engine.connect()
from sqlalchemy import select
select_stat = select([user_table.c.name,user_table.c.fullname]).where(
    user_table.c.name == 'qing'
)
results = conn.execute(select_stat)
for row in results:
    print(row)
