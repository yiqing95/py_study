__author__ = 'yiqing'
"""
Note that there is also an io.BytesIO class with similar behavior to StringIO,
 but which maps file
operations to an in-memory bytes buffer, instead of a str string:

better suited for scripts that deal with binary data
"""
from io import BytesIO

stream = BytesIO()
stream.write(b'spam')
print(
    stream.getvalue()
)

stream = BytesIO(b'dpam')
print(
    stream.read()
)