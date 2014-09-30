__author__ = 'yiqing'

import os
print(os.getpid())

## 获取当前工作目录
print(os.getcwd())

## 切换工作空间
os.chdir(r'C:\Users')
print(os.getcwd())