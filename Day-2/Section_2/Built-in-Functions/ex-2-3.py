numbers = [1, -2, 3]

print(any(n < 0 for n in numbers))  # True → at least one negative
print(all(n > 0 for n in numbers))  # False → not all positive
