__author__ = 'yiqing'

import  uuid

class DescriptorInstanceStorage(object):
    '''
    Descriptor that stores attribute data in instances

    '''

    def __init__(self,default = None):
        print('the descriptor is being inited ')
        # unique name with uuid
        self.hidden_name = '__'+uuid.uuid4().hex
        self.default = default

    def __get__(self, instance, owner):
        return getattr(instance,self.hidden_name,self.default)

    def __set__(self, instance, value):
        setattr(instance,self.hidden_name,value)


if __name__ == '__main__':
    class StoreInstance(object):
        """
        All instance will have its own 'attr'
        attr act as a singleton instance !!!
        """
        attr = DescriptorInstanceStorage(10)

        print('see what locals contains ?\n ',locals())

    s1 = StoreInstance()
    s2 = StoreInstance()
    print('store1',s1.attr)
    print('store2',s2.attr)
    print('setting the store1 ')
    s1.attr = 1000
    print('store1',s1.attr)
    print('store2',s2.attr)

    print('see what happens to store 1 ')
    print(s1.__dict__)
    print(s2.__dict__)
    print('you see the dictionary of s2 is empty !!!'
          ' \n if you do a setting on the attr of s2 the'
          '\t result will be obviouse '
          ' ')
    #
    print('\n',getattr(s2,'attrX','this is a default val for the attrX'))