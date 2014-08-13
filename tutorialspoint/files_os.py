__author__ = 'yiqing'
"""
os 模块提供了文件操作相关的函数，如重命名 删除文件等功能

"""

import  os
# 文件是否存在!
if os.path.isfile('foo.txt') or os.path.exists('foo.txt'):
    print('yes the foo.txt file exists!')

# since py3.4
import  pathlib
if(pathlib.Path('foo.txt').exists()):
    print('the file foo.txt is exists! ')

# 重命名！
if (os.path.isfile('foo.txt')):
    os.rename('foo.txt','my_new_name.txt')

# 新建并打开一个文件
tmp_file = open('tmp.txt','w+')
tmp_file.write("this is the file content")
read_str = tmp_file.read()
print('the file content in the temp file :',read_str)
tmp_file.close()

choice = input('do you want to delete the temp file ?')
if choice == 'yes':
    # 删除该临时文件
    os.remove('tmp.txt')
else:
    print('you do not want to delete this temp file !!')


#  文件夹操作：
try:
    os.mkdir('temp_dir')
except FileExistsError:
    print('the dir: temp_dir has been created !')
current_working_dir = os.getcwd()
print(current_working_dir)
os.chdir('temp_dir')
print('now the dir is :',os.getcwd())
# 在切换回来！
os.chdir(current_working_dir)

# 删除目录
os.rmdir('temp_dir')