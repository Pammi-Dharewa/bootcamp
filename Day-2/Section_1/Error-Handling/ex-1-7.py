from contextlib import suppress

d = {"a": 1}
with suppress(KeyError):
    print(d["b"])  # No KeyError shown, just silently ignored
print("Continued after suppress")
