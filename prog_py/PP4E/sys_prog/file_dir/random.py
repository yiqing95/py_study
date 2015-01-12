__author__ = 'yiqing'

records = [bytes([char] * 8) for char in b'spam']
print(records)

file = open('random.bin','w+b')
for rec in records:
    size = file.write(rec)

file.flush()
pos = file.seek(0)
print(
    file.read()
)