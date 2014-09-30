__author__ = 'yiqing'

import os
# 以写模式打开管道 像其他程序写数据
pipe = os.popen('python hello-in.py','w')
pipe.write('Gumby\n')

pipe.close()
print(
    open('hello-in.txt').read()
)