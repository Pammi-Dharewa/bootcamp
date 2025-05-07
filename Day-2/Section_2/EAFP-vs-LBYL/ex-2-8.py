def uppercase(s):
    if isinstance(s, str):  # LBYL
        return s.upper()
    else:
        return s

print(uppercase("hello"))  # HELLO
print(uppercase(42))       # 42
