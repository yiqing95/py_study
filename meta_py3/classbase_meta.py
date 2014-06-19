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

class StructMeta(type):
    def __new__(cls,name, bases,clsdict):
        clsobj = super().__new__(cls,name,bases,clsdict)
        sig = make_signature(clsobj._fields)
        setattr(clsobj,'__signature__',sig)
        return clsobj

class Structure(metaclass = StructMeta):
    _fields = []
    def __init__(self,*args,**kwargs):
        bound = self.__signature__.bind(*args,**kwargs)
        for name ,val in bound.arguments.items():
            setattr(self,name,val)

class User(Structure):
    _fields = ['name',
               'sex',
               'age'
               ]

if __name__ == '__main__':
    import inspect
    print(inspect.signature(User))