# Closure Function:
# Create a function make_multiplier(n) that returns another function.


def make_multiplier(n):
    def multiplier(x):
        return n * x
    return multiplier

triple = make_multiplier(3)
print("Triple of 10:", triple(10))  # 30
