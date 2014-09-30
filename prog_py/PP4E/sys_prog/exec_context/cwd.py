__author__ = 'yiqing'
"""
从不同的地方运行这个文件 会得到不同的结果的
如 C:\temp> python C:\...\PP4E\Tools\cleanpyc.py

程序的当前工作目录 可以始于你双击某个入口文件的地方！
"""
import os, sys
print(
    'my os.getcwd=> ' , os.getcwd()
)
# 注意当前目录被添加到系统搜索路径的首部了！！
print('my sys.path=> ' , sys.path)

input()