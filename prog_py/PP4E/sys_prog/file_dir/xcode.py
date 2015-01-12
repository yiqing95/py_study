__author__ = 'yiqing'

data = 'sp\xe4m'
print(
    data
)

print(
    0xe4,
    bin(0xe4),
    chr(0xe4),
)

print(
    data.encode('latin1'),
    data.encode('utf8'),
    # data.encode('ascii')
    data.encode('utf16'),
    data.encode('cp500')
)

open('data.txt','w',encoding='latin1').write(data)
print(
    open('data.txt','r',encoding='latin1').read()
)
print(
    open('data.txt','rb').read()
)