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

if __name__ == '__main__':
    run_tests()
