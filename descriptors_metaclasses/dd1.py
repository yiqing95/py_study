__author__ = 'yiqing'

'''
A typical data descriptor
'''

class DataDescriptor(object):
    '''
    A simple descriptor
    '''
    def __init__(self):
        self.value = 0

    def __get__(self, instance, owner):
        print('data descriptor __get__')
        return self.value
    def __set__(self, instance, value):
        print('data descriptor __set__')
        try:
            self.value = value.upper()
        except AttributeError:
            self.value = value
    def __delete__(self, instance):
            print( "Don't like to be deleted")

class NonDataDescriptor(object):
    def __init__(self):
        self.value = 0

    def __get__(self, instance, owner_cls):
        print('non data descriptor')
        return self.value + 10

if __name__ == '__main__':
    class Strange(object):
        attr = DataDescriptor()

    s = Strange()
    s.attr = 1
    print(s.attr)
    del s.attr
    #
    print(type(s).__dict__['attr'].__get__(s,type(s)))

    print(Strange.__dict__['attr'].__get__(s,Strange))

    print(Strange.attr)

    # class dictionary
    print(Strange.__dict__)
    # instance dic
    print(s.__dict__)
    s.anyKey = 'anyVal'
    print(s.anyKey)
    print(s.__dict__)
    print(dir(s))

    class AddTen(object):
        attr = NonDataDescriptor()

    ten = AddTen()
    print(ten.attr)
    print(ten.__dict__)
    try:
        # 由于没有复写__set__ 方法所以 转为原始用法了！！
        # 就是说 碰到属性 读 会先所属类中找（发现没有定义__set__），再操作自己的字典找 ？
        ten.attr = 3
        print(ten.__dict__)
    except Exception as ex:
        print(ex)


    class Overridden(object):
        attr = DataDescriptor()
        # 这个优先级高啊
        def __getattribute__(self, item):
            print('no Way! you want get %s'%item)

    o = Overridden()
    print(o.attr,o.attr2)


    class A(object):
        def func(self):
            print(self)
            pass

    a = A()
    # 一个是绑定了的
    print(a.func)
    # 一个是未绑定的
    print(A.func)
    print(type(A.func))
    print(type(a.func))
    A.func(a)
    a.func()
