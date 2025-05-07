# Keyword-Only Args: Define a function using * to enforce keyword-only arguments.

def keyword_only(*, a, b):
    print(f"a={a}, b={b}")

keyword_only(a=1, b=2)   # Works
# keyword_only(1, 2)     # Error: must use keywords
