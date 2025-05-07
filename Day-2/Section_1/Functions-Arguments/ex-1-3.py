# Variable Positional Args: Write def add_all(*args) to return the total.

def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3))    # 6
print(add_all(10, 20))     # 30
