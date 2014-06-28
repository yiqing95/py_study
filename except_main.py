__author__ = 'yiqing'

from exception import MyException

def sep():
    print('_'*45)

def my_except_test():
    try:
        raise MyException
    except :
        print('测试触发自定义异常')
    finally:
        print('this will be executed always ! ')

def assetTest():
    assert 1==1,'1 is not equal to 1 !'
    assert False,'this is the msg when the asset failed! '

if __name__ == '__main__':
    my_except_test()
    sep()

    try:
        assetTest()
    except Exception as ex:
       pass #  print(ex)
