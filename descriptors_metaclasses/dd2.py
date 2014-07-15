__author__ = 'yiqing'

class DescriptorClassStorage(object):
    '''
    Descriptor storing data in class
    '''

    def __init__(self,default=None):
        self.value = default

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

if __name__ == '__main__':
    class StoreClass(object):
        '''
        all instances will share 'attr'.
        '''
        attr = DescriptorClassStorage(10)

    s1 = StoreClass()
    s2 = StoreClass()

    print('store1',s1.attr)
    print('store2',s2.attr)

    print('setting s1 only :')
    s1.attr = 100
    print('store1',s1.attr)
    print('store2',s2.attr)
    s2.attr = 3
    print('store1',s1.attr)
    print('store2',s2.attr)
    print('the above running result prove that'
          ' the attr is class attribute !!!! '
          '')

