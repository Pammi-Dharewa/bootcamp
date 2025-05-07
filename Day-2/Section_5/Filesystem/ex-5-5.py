import tempfile

with tempfile.NamedTemporaryFile(delete=False) as tmp:
    tmp.write(b"Temporary data")
    print(f"Temporary file created at: {tmp.name}")
