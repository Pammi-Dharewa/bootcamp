nums = iter([1, 2, 3, 4])
a, b = itertools.tee(nums)
print(list(a))  # [1, 2, 3, 4]
print(list(b))  # [1, 2, 3, 4]
