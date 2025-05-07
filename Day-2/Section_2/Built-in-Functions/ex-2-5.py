nums = [1, 2, 3, 4]

doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8]

odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)  # [1, 3]
