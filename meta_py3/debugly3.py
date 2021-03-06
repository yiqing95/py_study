__author__ = 'yiqing'

from functools import wraps,partial

def debug( func=None, *, prefix=''):
    if func is None:
        return partial(debug,prefix=prefix)

    msg = prefix + func.__qualname__
    # func is function to be wrapped
    @wraps(func)
    def wrapper(*args,**kwargs):
        #  print(func.__qualname__)
        print(msg)
        return func(*args,**kwargs)
    return wrapper

'''
    装饰器作用在整个类之上 基本思想是遍历class的内部属性字典
    然后遍历所有属性 如果属性是callable性质的 就再其上调用
    debug方法 复写掉原始的方法定义
'''
def debugmethods(cls):
    # cls is a class
    for name,val in vars(cls).items():
        if callable(val):
            setattr(cls,name,debug(val))
    return cls
