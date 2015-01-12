__author__ = 'yiqing'

open('spam.txt','w').write('hello stat world \n')

import  os

info = os.stat('spam.txt')
print(
    info,
    info.st_atime,
    info.st_size
)

import stat
print(
    stat.ST_MODE,
    stat.ST_SIZE
)

print(
    stat.S_ISDIR(info.st_mode),
    stat.S_ISREG(info.st_mode)
)
# 等价的os模块调用：
path = 'spam.txt'
print(
    os.path.isdir(path),
    os.path.isfile(path),
    os.path.getsize(path)
)