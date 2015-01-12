__author__ = 'yiqing'

file = open('random.bin','r+b')
print(file.read())

record = b'X'*8
file.seek(0)
file.write(record)
print(
    ## not flushed!
    file.write(record),
    file.read(),
)
# file.flush()
# print(file.read())
file.seek(len(record)*2)
file.write(b'Y'*8)

file.seek(8) # 移动文件指针
file.read(len(record)) # 读取定长的字符串

print(
    file.read(len(record))
)