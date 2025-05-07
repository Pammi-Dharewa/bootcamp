def make_adder(n):
    return lambda x: x + n

add_five = make_adder(5)
print(add_five(10))  # 15
