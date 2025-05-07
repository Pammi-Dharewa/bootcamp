funcs = [abs, str, hex]
for f in funcs:
    print(f(f(-42)))
# abs(-42) → 42
# str(-42) → '-42'
# hex(-42) → '-0x2a'
