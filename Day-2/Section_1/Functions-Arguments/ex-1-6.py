# Positional-Only Args: Define a function using / to enforce positional arguments.

def pos_only(a, b, /):
    print(f"a={a}, b={b}")

pos_only(1, 2)       # Works
# pos_only(a=1, b=2)  # Error: must be positional
