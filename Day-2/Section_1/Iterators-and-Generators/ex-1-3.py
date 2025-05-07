it = iter([1, 2])

try:
    print(next(it))  # 1
    print(next(it))  # 2
    print(next(it))  # Raises StopIteration
except StopIteration:
    print("Iteration finished")
