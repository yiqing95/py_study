__author__ = 'yiqing'

file = open('data.txt','w')
file.write('hello file world!\n')

file.write('Bye file world . \n')

file.writelines(
    [
        'hello file world again!\n ',
        'bye file world!\n ',
    ]
)
### Closing is a generally harmless but robust habit to
### form.
file.close()

'''
文件的 上下文管理器
with
等价 try:
     finally 形式
'''
with open('data.txt') as tmpFile:
    print(
        tmpFile.read()
    )