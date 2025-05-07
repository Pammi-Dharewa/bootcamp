import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write(b'Hello temporary file!')
    temp.seek(0)
    print(temp.read())
