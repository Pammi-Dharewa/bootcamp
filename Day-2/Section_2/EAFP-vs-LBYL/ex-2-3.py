try:
    with open("nonexistent.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
