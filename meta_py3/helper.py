__author__ = 'yiqing'


'''
    打印分割线 用来在控制台方便阅读信息的
'''
def printHr():
    print('-' * 40)


'''
错误调用
'''
def errorCall(func,*args,**kwargs):
    if callable(func):
        try:
            func(*args,**kwargs)
        except:
            print('错误调用哦！')