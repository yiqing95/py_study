__author__ = 'yiqing'

import sys
## 被导入的模块们
'''
这算一个钩子 可以依次去对这些module做些什么？
'''
print(sys.modules)

print(list(sys.modules.keys()))

print(sys)
print(sys.modules['sys'])

## 内置的模块名
print(sys.builtin_module_names)

## 读取最近一次触发的异常信息
try:
    raise  IndexError
except:
    print(sys.exc_info())

###
import traceback
def grail(x):
    raise TypeError('already got one')

try:
    grail('arthur')
except:
    exc_info = sys.exc_info()
    print(exc_info[0])
    print(exc_info[1])
    ## 格式化消息
    traceback.print_tb(exc_info[2])

'''
此外sys还暴露：argv
stdin stdout stderr 等重要属性
sys.exit方法
'''