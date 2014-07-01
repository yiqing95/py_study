__author__ = 'yiqing'

from sqlalchemy import create_engine

engine  =  create_engine('sqlite:///mytest.db')
# engine  =  create_engine('sqlite:////..../mytest.db')
print(engine)
sql_create_table = '''
CREATE TABLE employee (
  id integer primary key autoincrement,
  name varchar
)
'''
# engine.execute(sql_create_table)

def print_employees(engine):
    results = engine.execute('SELECT * FROM employee ')
    '''
    for row in results:
        print(row)
    '''
    print(results.fetchall())

engine.execute('INSERT INTO employee(name) values (:name) ',name='yii')

print_employees(engine)

conn = engine.connect()
rslts = conn.execute('select * from employee ')
rows = rslts.fetchall()
print(rows)
conn.close()

with engine.begin() as conn:
    conn.execute("insert into employee(name) values(:name) ",name='hi')
    conn.execute("update employee set name= :name where name = :oldname ",name='hi2' , oldname='hi')
    print_employees(engine)