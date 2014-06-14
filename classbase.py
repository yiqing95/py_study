__author__ = 'yiqing'



'''
    这种做法的缺点是
    子类构造方法的参数 不能被其他工具探测 ！IDE也不能智能提示
    不能以k=v 形式传参
'''
class Structure:
    _fields = []
    def __init__(self , *args):
        for name , val in zip(self._fields,args):
            setattr(self,name,val)

class Stock(Structure):
    _fields = ['name','shares','price']

class Point(Structure):
    _fields = ['x','y']

class Address(Structure):
    _fields = ['hostname','port']


if __name__ == '__main__':
    import inspect
    print(inspect.signature(Address))