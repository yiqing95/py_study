__author__ = 'yiqing'

from inspect import Signature , Parameter

def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names
    )

#  做一个decorator：
def add_signature(*names):
    def dec(cls):
        cls.__signature__ = make_signature(names)
        return cls
    return dec

'''
    这种做法的缺点是
    子类构造方法的参数 不能被其他工具探测 ！IDE也不能智能提示
    不能以k=v 形式传参
'''
class Structure:
    __signature__ = make_signature([])
    def __init__(self , *args,**kwargs):
        bound = self.__signature__.bind(*args,**kwargs)
        for name , val in zip(self._fields,args):
            setattr(self,name,val)

class Stock(Structure):
    __signature__ = make_signature(['name','shares','price'])

class Point(Structure):
    __signature__ = make_signature(['x','y'])

class Address(Structure):
    __signature__ = make_signature(['hostname','port'])

@add_signature('name','sex','age')
class User(Structure):
    pass

if __name__ == '__main__':
    import inspect
    print(inspect.signature(Address))

    print(inspect.signature(User))