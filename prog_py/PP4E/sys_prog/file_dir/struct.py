__author__ = 'yiqing'
"""
The struct module provides calls to pack and unpack binary data, as though the data
was laid out in a C-language struct declaration. It is also capable of composing and
decomposing using any endian-ness you desire (endian-ness determines whether the
most significant bits of binary numbers are on the left or right side). Building a binary
datafile, for instance, is straightforward—pack Python values into a byte string and
write them to a file. The format string here in the pack call means big-endian (>), with
an integer, four-character string, half integer, and floating-point number:
"""
import struct
data = struct.pack(
    '>i4shf',
    '2',
    'spam',
    3,
    1.234,
)
print(data)

file = open('data.bin','wb')
file.write(data)
file.close()