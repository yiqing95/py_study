__author__ = 'yiqing'
"""
注意python 类 中定义的方法 第一个参数 往往是self 自己的意思
"""
class MyMeta(type):
    def __init__(cls,name,bases,cls_dict):
        """
        init  跟 new 的方法签名不一样 比之少一个metaclass 参数！
        new 覆盖不常用 反而经常见到覆盖这个init
        """
        print('class :',cls)
        print('class name:',name)
        print('class base tuple::',bases)
        print('class dictionary:',cls_dict)

        super(MyMeta,cls).__init__(name,bases,cls_dict)

class A(metaclass = MyMeta):
    pass

a = A()