__author__ = 'yiqing'
file  = open('random.bin','r')
reclen = 8
file.seek(reclen*3)
print(file.read(reclen))

file.seek(reclen*1)
print(
    file.read(reclen)
)

file = open('random.bin','rb')
file.seek(reclen*2)
print(file.read(reclen))