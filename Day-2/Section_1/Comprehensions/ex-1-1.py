# List Comprehension with Condition:
# From [1, 2, 3, 4], make [4, 16].

nums = [1, 2, 3, 4]
result = [n * n for n in nums if n % 2 == 0]
print("Squares of evens:", result)  # [4, 16]
