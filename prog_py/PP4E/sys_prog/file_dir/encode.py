__author__ = 'yiqing'

data = 'sp\xe4m'
print(
    data,
    len(data)
)

f = open('test',mode='w+',encoding='utf8')
f.write(data)
f.flush()
f.seek(0); print(f.read(1))

f.seek(2);print(f.read(1))

print(data[3])

f.seek(3);print(f.read(1))