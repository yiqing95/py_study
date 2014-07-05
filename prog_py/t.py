__author__ = 'yiqing'

'''
打印分割符
'''
def print_sep():
    print('='*45)

def call_str_func(func_name):
    '''
    通过一个字符串来调用相应的函数
    这个应该可以用eval！
    '''
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(func_name)

    if not method:
        return False
        # raise Exception("Method %s not implemented" % func_name)
    method()
    '''
    if type(method) != 'NoneType' and  callable(method):
        method()
    else:
        # pass
       return False
    '''

def run_tests():
    funcs  = ['test_'+str(i) for i in range(10)]
    # print(funcs)
    for func in funcs:
        print_sep()
        print('start calling the function %s : '%func)

        if  False == call_str_func(func):
            print('the %s is not a function name ' % func)

def test_1():
    print('this is the first test function')

def test_2():
    names = ['name','age','pay','job']
    values = ['Sue Jones',45,40000,'hdw']
    print(list(zip(names,values)))

    fields = ('name','age','job','pay')
    record = dict.fromkeys(fields,'?')
    print(record)

def test_3():
    bob = {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
    sue = {'job': 'hdw', 'pay': 40000, 'age': 45, 'name': 'Sue Jones'}
    people = [bob,sue]
    for person in people:
        print(person['name'],person['pay'],sep=', ')

    # 找某个指定人的工资
    for person in people:
        if person['name'] == 'Sue Jones':
            print(person['pay'])

    names = [person['name'] for person in people]
    list(map((lambda x:x['name']),people))

    # 工资求和
    print(sum(person['pay'] for person in people))

    print(
        [rec['name'] for  rec in people if rec['age'] >=45]
    )

    [(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people]
    G = (rec['name'] for rec in people if rec['age'] >= 45)
    next(G)
    G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
    G.__next__()

    # 更新：
    for person in people:
        print(person['name'].split()[-1]) # last name
        person['pay'] *= 1.10 # a 10% raise

    for person in people: print(person['pay'])

def test_4():
    bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
    sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')

    db = {}
    db['bob'] = bob
    db['sue'] = sue
    # pretty-printer
    import pprint
    pprint.pprint(db)
    for key in db:
        print(key,'=>',db[key]['name'])

    for record in db.values(): print(record['pay'])
    # 添加新人：
    db['tom'] = dict(name='Tom', age=50, job=None, pay=0)
    print(list(db.keys()))
    print(len(db))

    [rec['name'] for rec in db.values() if rec['age'] >= 45] # SQL-ish query

if __name__ == '__main__':
    run_tests()
