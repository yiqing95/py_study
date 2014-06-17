__author__ = 'yiqing'

from inspect import Signature , Parameter

class Descriptor:
    def __init__(self,name=None):
        self.name = name

    def __get__(self, instance, cls):
        # instance is the instance being manipulated
        # eg stock instance
        print('Get ',self.name)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("set ",self.name,value)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print("delete ",self.name)
        del instance.__dict__[self.name]

# 类型检测
class Typed(Descriptor):
    ty = object

    def __set__(self, instance, value):
        if not isinstance(value,self.ty):
            raise  TypeError('Expected %s' % self.ty)
        super().__set__(instance,value)

# 这个是正数检测
class Positive(Descriptor):
    def __set__(self, instance, value):
        if value < 0 :
            raise ValueError('Must be >= 0')
        super().__set__(instance,value)



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

class Integer(Typed):
    ty = int

class Float(Typed):
    ty = float

class String(Typed):
    ty = str

#-----------------------------------------------------#
'''
     注意继承顺序是很重要的 后面类的正确工作基于前面的类型判断
'''
# 想同时运用多种检测  那么用多继承！！！
class PositiveInteger(Integer,Positive):
    pass

class PositiveFloat(Float,Positive):
    pass
#-----------------------------------------------------#

class User(Structure):
    _fields = ['name','sex','age','height']
    name = String('name')
    sex = Integer('sex')
    # height = Float('height')
    height = PositiveFloat('height')

if __name__ == '__main__':
    u = User('yiqing',1,age=30,height=1.75)
    # 上面已经进行了类型检测  下面测试：
    u.name = 'yiqing95'
    try:
        u.sex = '1'
    except TypeError:
        print('需要整形哦！')

    print(u.__dict__)
    try :
        u.height = -1.5
    except:
        print('身高不能是负值哦 你是土行孙么?')

    # 方法解析顺序：
    print(User.__mro__)
    print(PositiveFloat.__mro__)