import sys

for line in sys.stdin:
    cleaned = line.strip()
    uppercased = cleaned.upper()
    print(uppercased)
