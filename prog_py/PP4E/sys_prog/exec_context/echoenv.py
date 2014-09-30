__author__ = 'yiqing'

"""
测试下 命令行下：

cmd> set USER=Bob
cmd> python echoenv.py

In general terms, a spawned program always
inherits environment settings from its parents.

单向传递 子进程可以读父传递的环境变量值 父不能读子

"""
import os
print('echoevn...',end='')

print('Hello,',os.environ['USER'])