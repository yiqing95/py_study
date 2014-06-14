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

'''
    debug 实例的属性
    重写类的某个属性即可！
'''
def debugattr(cls):
    orig_getattribute = cls.__getattribute__

    def __getattribute__(self,name):
        print('Get: ',name)
        return orig_getattribute(self,name)
    cls.__getattribute__ = __getattribute__
    # 返回修改过后的类
    return cls

'''
    想修饰所有类的简单做法
    对元类 下手！
'''
class debugmeta(type):
    def __new__(cls, clsname,bases,clsdict):
        clsobj = super().__new__(cls,clsname,
                                 bases,clsdict)
        clsobj = debugmethods(clsobj)
        return  clsobj