__author__ = 'yiqing'

class MyMeta_(type):
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)

class MyMeta(type):
    def __new__(meta_cls, name,bases,cls_dict):
        print('meta class: ',meta_cls)
        print('class name: ',name)
        print('bases tuple: ',bases)
        print('class dictionary: ',cls_dict)
        """
       上面的打印语句 在正式应用中实际可以作为钩子点 注入某些逻辑进去的！比如修改类字典
       为函数 添加decorator ！
       """
        # 如果没有下面这行 那么用此类作为元类型的类 将无法被使用！！！
        # return type.__new__(meta_cls,name,bases,cls_dict)
        # !!! NOTE 错误的 return super.__new__(meta_cls,name,bases,cls_dict)
        print(super())
        print('parent class :',super(MyMeta,meta_cls))
        return super(MyMeta,meta_cls).__new__(meta_cls,name,bases,cls_dict)

class A(metaclass=MyMeta):
    pass

a = A()

"""
请看下回 mt4.py
"""