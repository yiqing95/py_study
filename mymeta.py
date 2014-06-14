__author__ = 'yiqing'

'''
    定义自己的元类型
    py中类型体系是这样的：
    所有的class 都是type的实例
    （type是自己的实例---可能有误！）
    所有对象时某个class 的实例
'''
class mytype(type):
    '''
    通过判断bases的数量 可以达到单继承的约束限制:
    if(len(bases)>1):
        raise xxx

    '''
    def __new__(cls, name,bases,clsdict):
        clsobj = super().__new__(cls,
                                 name,
                                 bases,
                                 clsdict
                                 )
        return clsobj