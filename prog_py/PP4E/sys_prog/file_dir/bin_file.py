__author__ = 'yiqing'

open('data.bin','wb').write(b'Spam\n')

print(
    open('data.bin','rb').read()
)

try:
    open('data.bin','wb').write('spam\n')
except:
    print(
        'only byte string allowed!'
    )