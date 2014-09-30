__author__ = 'yiqing'

import os
##  操作系统可移植的做法！

print(
    os.path.isdir(r'C:\Ustrs'),
   os.path.isfile(r'C:\Users'),
   os.path.exists(r'c:\Users\someFileName.any'),
   os.path.getsize(r'c:\Users')
)

## 分隔与拼接文件路径
print(
    os.path.split(r'C:\temp\data.txt'),
    os.path.join(r'C:\temp','output.data')
)
name = r'C:\temp\data.txt'
print(
    os.path.dirname(name),
    os.path.basename(name)
)

print(os.path.splitext(r'C:\PP4thEd\Examples\PP4E\PyDemos.pyw'))

###
print(os.sep)
pathname =r'C:\PP4thEd\Examples\PP4E\PyDemos.pyw';
print(os.path.split(pathname))

print(pathname.split(os.sep))

print(
    os.sep.join(pathname.split(os.sep))
)

###
print(os.path.join(*pathname.split(os.sep)))
## print(mixed)

print(os.path.normpath(r'C:\temp\\sub\.\file.ext'))