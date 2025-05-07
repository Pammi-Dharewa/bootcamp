def compose(f, g):
    return lambda x: f(g(x))

double = lambda x: x * 2
increment = lambda x: x + 1

composed = compose(double, increment)
print(composed(3))  # double(increment(3)) → double(4) → 8
