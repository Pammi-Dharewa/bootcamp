import contextlib

with contextlib.suppress(FileNotFoundError):
    with open('nonexistent.txt', 'r') as f:
        f.read()
print("Continued despite missing file")
