__author__ = 'yiqing'

import my_sqlalchemy.test1 as test1


if __name__ == '__main__':
    print("this is the app entry!")

    # import my_mysqldb.test1

    test1.table_test()
    # 第一次已经关闭连接了 第二次执行就出错啦！
    test1.table_test()